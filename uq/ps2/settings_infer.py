#!/bin/py
#
# global settings for the inference routines
# 


#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
from scipy.linalg import det, solve
from scipy.integrate import odeint
import numpy as np
from Data.read_data import read_data

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

def logGaussian(MEAN, COVAR, X):
	# Return the log of a multivariate Gaussian pdf evaluated at X
	# MEAN, X = np.arrays (kk, 1)
	# COVAR = np.array (kk, kk)
	kk = np.size(MEAN)
	assert np.size(MEAN) == np.size(X), "MEAN and X must have same size"

	# Handle scalar differently:
	if kk  == 1:
		return np.log(1.0 / np.sqrt(COVAR*2.0*np.pi)) - .5*(MEAN-X)**2 / COVAR

	try:
		colsize = np.shape(MEAN)[1]
	except:
		MEAN = MEAN.reshape((kk, 1))
		colsize = np.shape(MEAN)[1]

	assert colsize == 1, "MEAN must be column vector or a number"
	assert np.shape(MEAN) == np.shape(X), "MEAN and X must have same shape"
	assert np.size(COVAR) == kk**2, "MEAN and COVAR must have same nb of rows"

	detC = det(COVAR)
	MISFIT = MEAN - X
	invCM = solve(COVAR, MISFIT)
	return np.log(1.0 / np.sqrt(detC*(2.0*np.pi)**kk)) \
	- .5*np.dot(MISFIT.T, invCM)


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
guess_a = 0.75
guess_s = 1.0
guess_h = 35.0
guess_c = 1.0


#
# please now put these guesses into a list:
# (please ensure the order in which you guess is the same 
#  as the order for the prior_function list)
#
guess_list = [guess_a, guess_s, guess_h, guess_c]

#
# perturb q,c,p
#
perturb_a = 0.05
perturb_s = 0.3
perturb_h = 0.4
perturb_h = 0.5

perturb_list = [perturb_a, perturb_s, perturb_h, perturb_c]

#
# list of qoi (strings please)
# (please ensure this is identical to the order you placed in 'prior_funcs')
# (or else, labels could be misleading)
qoi_list = ["a", "s", "H", "C"]

# Load data and build elementary vectors and matrices for the
# mean and covariance of the likelihood function
DataFolder = 'Data/'
DataFiles = ['Basket_Ball_1.dat', 'Basket_Ball_2.dat', \
'Bowling_Ball_1.dat', 'Bowling_Ball_2.dat']
DTIMES = []
DHEIGHTS = []
# NOTE: We here exclude the last measurement as it looked suspicious
# on the plots (we believe the ball is boucing)
for myfile in DataFiles:
	t, h = read_data(DataFolder + myfile)
	DTIMES.append(np.array(t[:-1]))
	DHEIGHTS.append(np.array(h[:-1]))

tau = 0.5	# Factor in covariance matrix of Likelihood
DCOVAR = []	# Covariance matrix for each experiment
for hh in DHEIGHTS:
	dimR = np.size(hh)
	COVAR = (np.zeros(dimR**2)).reshape((dimR, dimR))
	for ii in range(dimR):
		COVAR[ii,:] = np.exp(-np.abs(hh - hh[ii])/tau)
	DCOVAR.append(COVAR)
