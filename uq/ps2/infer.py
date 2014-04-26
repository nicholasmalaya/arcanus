#!/usr/bin/env python
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import pylab
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
from scipy import stats
import sys

# local files that will be imported
import likelihood
from settings_infer import *
from prior import *

# -------------------------------------------------------------
# subroutine that generates a .pdf file plotting a prior and posterior quantity
# -------------------------------------------------------------
def plotter(chain,ind,xmin=None,xmax=None):
    from math import log, pi
    bins = np.linspace(np.min(chain), np.max(chain), 200)
    qkde = stats.gaussian_kde(chain)
    qpdf = qkde.evaluate(bins)

    # plot posterior
    pyplot.figure()
    pyplot.plot(bins, qpdf, linewidth=3, label="Post")

    # plot prior (requires some cleverness to do in general)
    qpr  = [prior_funcs[i](x) for x in bins]
    qpri = [np.exp(x) for x in qpr]        
    qpri=qpri/np.linalg.norm(qpri) 
    pyplot.plot(bins, qpri, linewidth=3, label="Prior")

    # user specified bounds to x-range:
    if(xmin != None and xmax != None):
        bounds = np.array([xmin, xmax])
        pyplot.xlim(bounds)        

    quant = qoi_list[i]
    pyplot.xlabel(quant, fontsize=30)
    pyplot.ylabel('$\pi('+quant+')$', fontsize=30)
    pyplot.legend(loc='upper left')
    pyplot.savefig(quant+'_post.pdf', bbox_inches='tight')
   
# -------------------------------------------------------------
# MCMC sampling Function
# -------------------------------------------------------------

class BayesianRichardsonExtrapolation(object):
    "Computes the Bayesian Richardson extrapolation posterior log density."

    def __call__(self, params, dtype=np.double):

        from math import log

        print params[0], params[1], params[2]
        return (
            prior(params) + 
            likelihood.likelihood(params)
            )

# -------------------------------------------------------------
# Main Function
# -------------------------------------------------------------
#
# Stop module loading when imported.  Otherwise continue running.
if __name__ != '__main__': raise SystemExit, 0

# Example of sampling Bayesian Richardson extrapolation density using emcee
from emcee import EnsembleSampler
from math import ceil, floor, sqrt

#
# initalize the Bayesian Calibration Procedure 
#
bre = BayesianRichardsonExtrapolation()

print("\nInitializing walkers")
nwalk = 100
params0       = np.tile(guess_list, nwalk).reshape(nwalk, len(guess_list))
#
# perturb walkers around guess
#
for i in xrange(len(guess_list)):
    params0.T[i] += np.random.rand(nwalk) * perturb_list[i]

# hack!
params0.T[2]  = np.absolute(params0.T[2])        # ...and force >= 0

print("\nInitializing the sampler and burning in walkers")
s = EnsembleSampler(nwalk, params0.shape[-1], bre, threads=4)
pos, prob, state = s.run_mcmc(params0, burn_in)
s.reset()

print("\nSampling the posterior density for the problem")
s.run_mcmc(pos, samples)
print("Mean acceptance fraction was %.3f" % s.acceptance_fraction.mean())

#
# 1d Marginals
#
print("\nDetails for posterior one-dimensional marginals:")
print((10*" %15s") % ("", "min", "P5", "P25", "P50", "P75", "P95", "max", "mean", "stddev"))
def textual_boxplot(label, unordered):
    n, d = np.size(unordered), np.sort(unordered)
    print((" %15s" + 9*" %+.8e") % (label,
                                    d[0],
                                    d[[floor(1.*n/20), ceil(1.*n/20)]].mean(),
                                    d[[floor(1.*n/4), ceil(1.*n/4)]].mean(),
                                    d[[floor(2.*n/4), ceil(2.*n/4)]].mean(),
                                    d[[floor(3.*n/4), ceil(3.*n/4)]].mean(),
                                    d[[floor(19.*n/20), ceil(19.*n/20)]].mean(),
                                    d[-1],
                                    d.mean(),
                                    d.std()))
    return d.mean(), 2*d.std()

box_mean = []
box_std  = []
for i in xrange(len(qoi_list)):
    mm, ss = textual_boxplot(qoi_list[i], s.flatchain[:,i])
    box_mean.append(mm)
    box_std.append(ss)

#----------------------------------
# FIGURES: Marginal posterior(s)
#----------------------------------
print("\nPrinting PDF outputs")
for i in xrange(len(qoi_list)):
    plotter(s.flatchain[:,i],i)

#----------------------------------
# FIGURE: Joint posterior(s)
#----------------------------------
#
qbins  = []
qkde   = []
qpdf   = []
bounds = []
qticks = []

for i in xrange(len(qoi_list)):
    qbins.append(np.linspace(np.min(s.flatchain[:,i]), np.max(s.flatchain[:,i]), 200))
    qkde.append(stats.gaussian_kde(s.flatchain[:,i]))
    qpdf.append(qkde[i].evaluate(qbins[i]))
    bounds.append(np.array([box_mean[i]-box_std[i],box_mean[i]+box_std[i]]))
    qticks.append(np.linspace(bounds[i][0], bounds[i][1], 3))

pyplot.figure()

from matplotlib.ticker import MultipleLocator, FormatStrFormatter
formatter = FormatStrFormatter('%5.4f')
formatter2 = FormatStrFormatter('%5.f')

col = len(qoi_list)
for i in xrange(col):
    for j in xrange(col):
        if(j>=i):
             pylab.subplot(col,col,(j+i*col)+1)

             # plot marginal
             if (j == i):
                 pyplot.plot(qbins[i], qpdf[i], linewidth=2, color="k", label="Post")
                 pyplot.xlim(bounds[i])
                 pylab.gca().set_xticks(qticks[i])
                 pylab.gca().xaxis.set_major_formatter(formatter)
                 pylab.gca().xaxis.set_minor_formatter(formatter)
                 pylab.gca().set_yticks([])
                 pyplot.xlabel(qoi_list[i], fontsize=24)

             # plot contour when j>i
             else:
                 H, qe, Ce = np.histogram2d(s.flatchain[:,i], s.flatchain[:,j], bins=(200,200))
                 qv = 0.5*(qe[0:-1] + qe[1:len(qe)]);
                 Cv = 0.5*(Ce[0:-1] + Ce[1:len(Ce)]);
                 pyplot.contour(Cv,qv,H,5,colors='k')
                 pyplot.xlim(bounds[j])
                 pylab.gca().set_xticks(qticks[j])
                 pylab.gca().set_xticklabels([])
                 pylab.gca().set_yticks(qticks[i])
                 pylab.gca().set_yticklabels([])

pyplot.savefig('joint_post.pdf', bbox_inches='tight')

