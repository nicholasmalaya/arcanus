#!/bin/py
#
#
import math

def press(q):
    rho = 0.074887
    cd  = 0.62
    d   = 1.8227
    D   = 4
    beta = d/D

    return rho/2 * ((q*(1-beta**4)**(0.5))/(cd*math.pi**2/4))**2

#
# output
# 
print '5 cfm  ', press(5), ' psi'
print '50 cfm ', press(50), ' psi'

#
# nick
# 9/15/15
#
