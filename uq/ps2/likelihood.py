#!/usr/bin/env python
#
import numpy as np
from settings_infer import *
import sys.exit(1)

#
# precompute whatever we can
#
t1 = np.linspace(0.0,2.9,43)
t2 = np.linspace(0.0,2.9,43)

#
# B  = bowling
# bb = basketball
#
g = 9.81334 
rho=1.4
rb =0.1166
rbb=0.1066
Mb =2.296
Mbb=.4548
tau=0.5

#
# load bowling ball data
#
tb1, hb1 = read_data('Bowling_Ball_1.dat')
tb2, hb2 = read_data('Bowling_Ball_2.dat')

#
# load basketball
#
tbb1, hbb1 = read_data('Basket_Ball_1.dat')
tbb2, hbb2 = read_data('Basket_Ball_2.dat')

#
# convert each element from 1/600 sec to time...
#
tb1  = tb1/600.0
tb2  = tb2/600.0

tbb1 = tbb1/600.0
tbb1 = tbb1/600.0

def likelihood(params):
    """
    This routine should return the log of the
    likelihood function: P(qi|q,C,p,X)
    """
    a, s, h, c = params

    #
    # form r's
    # 
    rb  = c*rho*4*np.pi*r1**2/(2*Mb)

    rbb = c*rho*4*np.pi*r2**2/(2*Mbb)
    
    if r < 0 or r2 < 0:
        print 'achtung! negative drag!'
        sys.exit(1)

    #
    # solve ode at each time
    #
    [h1,v2]=drag_eqn(t1,g,r)
    [h2,v2]=drag_eqn(t2,g,r2)

    

    
    likelihood = exponent - np.log((2*np.pi)**(n/2) * * (2*np.pi())**(n2/2) * D1 * D2)
    return likelihood
