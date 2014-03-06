#!/usr/bin/env python
#
import numpy as np
from settings_infer import *

def likelihood(params):
    """
    This routine should return the log of the
    likelihood function: P(qi|q,C,p,X)
    evaluated for given values of q, C and p
    """
    q, C, p = params
    
    H = np.array([2.0, np.sqrt(2.0), 1.0, 0.5])
    UCHTILDE = np.array([1.16828362427, 1.16429173392, 1.16367827195, 1.16389876649])
    SIGMAH = np.array([0.0001283, 0.0003982, 0.0001282, 0.0002336])
    likelihood = logGaussian(UCHTILDE, SIGMAH, q - C*H**p)

    return likelihood
