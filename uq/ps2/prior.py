#!/usr/bin/env python
#
import numpy as np
from settings_infer import *

def prior_U(q):
    """
    This routine should return the log of the 
    prior probability distribution: P(q|X)
    evaluated for the given value of q.
    """

    mymean = 1.1627
    myvar = 2.0*0.05*mymean / 3.92
    
    prior_U = logGaussian(mymean, myvar, q)
    return prior_U

def prior_C(C):
    """
    This routine should return the log of the 
    prior probability distribution: P(C|X)
    evaluated for the given value of C.
    """

    mymean = 0.0
    meanUc = 1.1627
    myvar = 2.0*0.005*meanUc / 3.92

    prior_C = logGaussian(mymean, myvar, C)
    return prior_C

def prior_p(p):
    """
    This routine should return the log of the 
    prior probability distribution: P(p|X)
	evaluated for the given value of p.
    """

    pmin = 1.0
    pmax = 10.0

    if (p >= pmin) and (p <= pmax):
        prior_p = -np.log(pmax-pmin)
    else:
        prior_p = -np.inf
        
    return prior_p

#
# here, please append each prior function for evaluation
#
# e.g. for two prior functions, prior_A(a) and prior_B(b)
#      
#    prior_funcs = [prior_A, prior_B] 
#    
# 
prior_funcs = [prior_U,prior_C,prior_p]

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
