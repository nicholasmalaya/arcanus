#!/usr/bin/env python
#
#

#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
from scipy.linalg import det, solve
from scipy.integrate import odeint
import scipy.stats
import numpy as np

def deriv(h,t,param): 
    """return derivatives of the array y"""
    g = 9.81334 
    rho=1.4
    g = param[0]
    r = param[1]
    return np.array([ h[1], -g + r * h[1]**2])

def drag_eqn(times,g,r):
    """define scenario and integrate"""
    param = np.array([ g, r])
    hinit = np.array([0.0,0.0])       # initial values (position and velocity, respectively)
    h = odeint(deriv,hinit,times, args = (param,))
    return h[:,0], h[:,1]

# -------------------------------------------------------------
# Main Function
# -------------------------------------------------------------
#
# Stop module loading when imported.  Otherwise continue running.
if __name__ != '__main__': raise SystemExit, 0

#
# load data into arrays
#
sigmas = [line.strip() for line in open('data/sigma_ds.dat')]
alphas = [line.strip() for line in open('data/sigma_ds.dat')]
drags  = [line.strip() for line in open('data/sigma_ds.dat')]

#
# convert to floats
#
sigma = map(float, sigmas)
alpha = map(float, alphas)
drag  = map(float, drags)

#
# params
#
tmin = 0.0
tmax = 3.0
tspacing = 40/600.

ymin = 0.0
ymax = 35.8
spacing = 0.1
yp    = np.arange(ymin,ymax,spacing)
times = np.arange(tmin,tmax,tspacing)
pr       = np.zeros(len(yp))
integral = np.zeros(len(yp))

#
# given a time (seconds)
#
t = 1.0
g = 9.81334 
rho=1.4
rb =0.1166
rbb=0.1066
Mb =2.296
Mbb=0.4548

coef_b  = (rho*4*np.pi*rb**2.0)/(2.0*Mb)
coef_bb = (rho*4*np.pi*rbb**2.0)/(2.0*Mbb)

#
# iterate over position
#

for i in xrange(len(yp)):
    
    #
    # iterate over mcmc chain
    #
    for j in xrange(len(drag)):
        mu = drag_eqn([t],g,coef_b*drag[i])[0]+alpha[j]*t
        integral[i] += scipy.stats.norm(mu, sigma[j]).pdf(yp[i])[0]

    #
    # normalize
    #
    integral /= len(drag)
    
    #
    # print
    #
    print yp[i], integral[i]


#
# nick
# 5/4/14
#
