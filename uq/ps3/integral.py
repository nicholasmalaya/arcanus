#!/usr/bin/env python
#
#

#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
from scipy.linalg import det, solve
from scipy.integrate import odeint
import scipy.stats
import numpy as np

def deriv(h,t,param): 
    """return derivatives of the array y"""
    #
    g = 9.81334 
    rho=1.4
    g = param[0]
    r = param[1]
    return np.array([ h[1], -g + r * h[1]**2])

# -------------------------------------------------------------
# Main Function
# -------------------------------------------------------------
#
# Stop module loading when imported.  Otherwise continue running.
if __name__ != '__main__': raise SystemExit, 0

#
# load data into arrays
#
sigma = [line.strip() for line in open('data/sigma_ds.dat')]
alpha = [line.strip() for line in open('data/sigma_ds.dat')]
drag  = [line.strip() for line in open('data/sigma_ds.dat')]

#
# choose yp grid (positions of observations)
#
ymin = 0
ymax = 10
spacing = 0.1
yp = np.arange(ymin,ymax,spacing)

#
# evaluate sum for each yp
# 
mu    = 0.0
sigma = 1.0

for i in yp:

    # mu is the data
    # sigma is less clear: 
    scipy.stats.norm(mu, sigma).pdf(i)

#
# nick
# 5/4/14
#
