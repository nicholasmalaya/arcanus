#!/bin/py
#
# global settings for the inference routines
# 


#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
from scipy.integrate import odeint
import numpy as np

def deriv(h,t,param): 
    """return derivatives of the array y"""
    g = param[0]
    r = param[1]
    return np.array([ h[1], -g + r * h[1]**2])

def drag_eqn(times,g,r):
    """define scenario and integrate"""
    param = np.array([ g, r])
    hinit = np.array([0.0,0.0])       # initial values (position and velocity, respectively)
    h = odeint(deriv,hinit,times, args = (param,))
    return h[:,0], h[:,1]

def logGaussian(MEAN, VAR, X):
	# Return the log of a multivariate Gaussian pdf evaluated at X
	kk = np.size(MEAN)

	if kk  == 1:
		return np.log(1.0 / (VAR*np.sqrt(2.0*np.pi))) - .5*(MEAN-X)**2 / VAR**2

	detS = VAR.prod()
	MISFIT = (MEAN - X)/VAR
	return np.log(1.0 / (detS*np.sqrt((2.0*np.pi)**kk))) \
	- .5*np.dot(MISFIT, MISFIT)

#
# this is how long the walkers will propagate, before we start
# to record statistics
burn_in = 5000

#
# number of samples to gather
#
samples = 10000


#
# initial guesses for the walkers starting locations
#
guess_q = 1.16389876649
guess_c = 0
guess_p = 6

#
# please now put these guesses into a list:
# (please ensure the order in which you guess is the same 
#  as the order for the prior_function list)
#
guess_list = [guess_q, guess_c, guess_p]


#
# perturb q,c,p
#
perturb_q = 0.025
perturb_c = 0.1
perturb_p = 1.5

perturb_list = [perturb_q, perturb_c, perturb_p]


#
# list of qoi (strings please)
#
qoi_list = ["U", "C", "p"]
