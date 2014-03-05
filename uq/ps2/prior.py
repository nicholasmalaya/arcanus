#!/usr/bin/env python
#
import numpy as np

def prior_U(q):
    """
    This routine should return the log of the 
    prior probability distribution: P(q|X)
    evaluated for the given value of q.
    """

    return prior_U

def prior_C(C):
    """
    This routine should return the log of the 
    prior probability distribution: P(C|X)
    evaluated for the given value of C.
    """

    return prior_C

def prior_p(p):
    """
    This routine should return the log of the 
    prior probability distribution
    """

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
def prior(q,C,p):
    """
    This routine should return the log of the
    prior probability distribution.
    """

    # for some reason the p guesses are sometimes negative, this 
    # patches that up
    if(p < 0):
        return -1 * np.inf

    #
    # python list comprehension will sum over each function 
    #        e.g. prior_A(a) + prior_B(B) + ... + prior_N(n)
    #
    return [f() for f in prior_funcs]
