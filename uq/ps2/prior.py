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
prior_funcs = []

#
# One should not have to edit the routine below
#
def prior(params):
    """
    This routine should return the log of the
    prior probability distribution.
    """
    q, C, p = params

    # for some reason the p guesses are sometimes negative, this 
    # patches that up
    if(p < 0):
        return -1 * np.inf

    #
    # python list comprehension will sum over each function 
    #        e.g. prior_A(a) + prior_B(B) + ... + prior_N(n)
    #
    #return [f() for f in prior_funcs]
    return prior_U(q) + prior_C(C) + prior_p(p)
