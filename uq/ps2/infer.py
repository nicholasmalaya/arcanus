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

        #print params[0], params[1], params[2]
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

#print("\nInitializing walkers")
nwalk = 100
params0       = np.tile(guess_list, nwalk).reshape(nwalk, len(guess_list))
#
# perturb walkers around guess
#
for i in xrange(len(guess_list)):
    params0.T[i] += np.random.rand(nwalk) * perturb_list[i]

# hack!
params0.T[2]  = np.absolute(params0.T[2])        # ...and force >= 0

#print("\nInitializing the sampler and burning in walkers")
s = EnsembleSampler(nwalk, params0.shape[-1], bre, threads=4)
pos, prob, state = s.run_mcmc(params0, burn_in)
s.reset()

#print("\nSampling the posterior density for the problem")
s.run_mcmc(pos, samples)

samplea = s.flatchain[:,0]
pylab.plot(samplea)
pylab.xlabel('Step number')
pylab.ylabel('alpha')
pylab.show()
pylab.savefig('alpha.png')

samples = s.flatchain[:,1]
pylab.plot(samples)
pylab.xlabel('Step number')
pylab.ylabel('sigma')
pylab.show()
pylab.savefig('sigma.png')

sample = s.flatchain[:,2]
pylab.plot(sample)
pylab.xlabel('Step number')
pylab.ylabel('Value')
pylab.show()
pylab.savefig('cd.png')

filepath='sigma.dat'
f = open(filepath, 'w')
for item in samples:
    f.write("%s\n" % item)

filepath='alpha.dat'
f = open(filepath, 'w')
for item in samplea:
    f.write("%s\n" % item)

filepath='drag.dat'
f = open(filepath, 'w')
for item in sample:
    f.write("%s\n" % item)
