#!/usr/bin/env python
#
import numpy as np
from settings_infer import *

def prior_a(a):
    """
	Log Prior for alpha
	"""

    mymean = 0.5
    myvar = 1
    
    return logGaussian(mymean, myvar**2, a)


def prior_S(s):
    """
	Log Prior for sigma
    """

    smin = 0.0
    smax = 2.0

    if (s >= smin) and (s <= smax):
        return -np.log(smax-smin)
    else:
        return -np.inf


def prior_H(h):
    """
	Log Prior for H
    """

    hmin = 34.5
    hmax = 35.5

    if (h >= hmin) and (h <= hmax):
        return -np.log(hmax-hmin)
    else:
        return -np.inf


def prior_C(c):
	"""
	Log Prior for C
	"""
	
	return assert False

#
# here, please append each prior function for evaluation
#
# e.g. for two prior functions, prior_A(a) and prior_B(b)
#      
#    prior_funcs = [prior_A, prior_B] 
#    
# 
prior_funcs = [prior_a, prior_s, prior_H, prior_C]

#
# One should not have to edit the routine below
#
def prior(params):
    """
    This routine should return the log of the
    prior probability distribution.
    """

    #
    # python list will sum over each function 
    #        e.g. prior_A(params) + prior_B(params) + ... + prior_N(params)
    #
    ss = 0.0
    for i in xrange(len(prior_funcs)):
        ss += prior_funcs[i](params[i])
    return ss
