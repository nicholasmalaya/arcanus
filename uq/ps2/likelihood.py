#!/usr/bin/env python
#
import numpy as np
from settings_infer import *
import sys

#
# B  = bowling
# bb = basketball
#
g = 9.81334 
rho=1.4
tau=0.5

rb =0.1166
rbb=0.1066

Mb =2.296
Mbb=.4548

#
# load bowling ball data
#
tb1, hb1 = read_data('Data/Bowling_Ball_1.dat')
tb2, hb2 = read_data('Data/Bowling_Ball_2.dat')

#
# load basketball
#
tbb1, hbb1 = read_data('Data/Basket_Ball_1.dat')
tbb2, hbb2 = read_data('Data/Basket_Ball_2.dat')

#
# convert each element from 1/600 sec to time...
#
tb1  = np.asarray(tb1)/600.0
tb2  = np.asarray(tb2)/600.0

tbb1 = np.asarray(tbb1)/600.0
tbb1 = np.asarray(tbb1)/600.0

nb1  = len(tb1)
nb2  = len(tb2)
nbb1 = len(tbb1)
nbb2 = len(tbb2)

#
# initalize covariance matricies as zeros
#
Rb1  = np.zeros((nb1,  nb1))
Rb2  = np.zeros((nb2,  nb2))

Rbb1 = np.zeros((nbb1,  nbb1))
Rbb2 = np.zeros((nbb2,  nbb2))

#
# now, iterate over each matrix element
#
for i in xrange(len(tb1)):
    for j in xrange(len(tb1)):
        Rb1[i][j] = np.exp(-abs(tb1[i]-tb1[j])/tau)

for i in xrange(len(tb2)):
    for j in xrange(len(tb2)):
        Rb2[i][j] = np.exp(-abs(tb2[i]-tb2[j])/tau)

for i in xrange(len(tbb1)):
    for j in xrange(len(tbb1)):
        Rbb1[i][j] = np.exp(-abs(tbb1[i]-tbb1[j])/tau)

for i in xrange(len(tbb2)):
    for j in xrange(len(tbb2)):
        Rbb2[i][j] = np.exp(-abs(tbb2[i]-tbb2[j])/tau)

def likelihood(params):
    """
    This routine should return the log of the
    likelihood function: P(qi|q,C,p,X)
    """
    a, s, H, c = params

    #
    # form r's (coefficient on ODE)
    # 
    coef_b  = (c*rho*4*np.pi*rb**2.0)/(2.0*Mb)
    coef_bb = (c*rho*4*np.pi*rbb**2.0)/(2.0*Mbb)
    
    #
    # sanity check
    #
    if rb < 0 or rbb < 0:
        print "achtung! negative drag!"
        sys.exit(1)

    #
    # solve ode at each time series
    #
    [hdb1,vb1]   = drag_eqn(tb1,g,coef_b)
    [hdb2,vb2]   = drag_eqn(tb2,g,coef_b)

    [hdbb1,vbb1] = drag_eqn(tbb1,g,coef_bb)
    [hdbb2,vbb2] = drag_eqn(tbb2,g,coef_bb)

    #
    # form \mu 
    #
    mub1  = a * tb1
    mub2  = a * tb2
    mubb1 = a * tbb1
    mubb2 = a * tbb2

    #
    # form actual covariance
    #

    sRb1  = s*s * Rb1
    sRb2  = s*s * Rb2
    sRbb1 = s*s * Rbb1
    sRbb2 = s*s * Rbb2

    #
    # calculate determinant
    #
    DRb1 = (np.linalg.det(sRb1))**0.5
    DRb2 = (np.linalg.det(sRb2))**0.5
    DRbb1= (np.linalg.det(sRbb1))**0.5
    DRbb2= (np.linalg.det(sRbb2))**0.5

    #
    # put it all together, and straight on till morning
    #    

    eb1   = -1/2 * ( 35*hdb1 /H - hb1 - mub1) * np.linalg.inv(sRb1) * ( 35*hdb1 /H - hb1 - mub1) 
    eb2   = -1/2 * ( 35*hdb2 /H - hb2 - mub2) * np.linalg.inv(sRb2) * ( 35*hdb2 /H - hb2 - mub2) 

    ebb1   = -1/2 * ( 35*hdbb1 /H - hb1 - mubb1) * np.linalg.inv(sRbb1) * ( 35*hdbb1 /H - hb1 - mubb1)
    ebb2   = -1/2 * ( 35*hdbb2 /H - hb2 - mubb2) * np.linalg.inv(sRbb2) * ( 35*hdbb2 /H - hb2 - mubb2) 

    #
    # likelihood
    #

    lb1 = eb1 - np.log((2*np.pi)**(nb1/2) * DRb1)
    lb2 = eb2 - np.log((2*np.pi)**(nb2/2) * DRb2)

    lbb1 = ebb1 - np.log((2*np.pi)**(nbb1/2) * DRbb1)
    lbb2 = ebb2 - np.log((2*np.pi)**(nbb2/2) * DRbb2)

    return lb1
