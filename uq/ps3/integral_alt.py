#!/usr/bin/env python
#
#
import sys
#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
from scipy.linalg import det, solve
from scipy.integrate import odeint
from scipy.integrate import simps
import scipy.stats
import numpy as np
from hpd import *


def deriv(h,t,param): 
	"""return derivatives of the array y"""
	g = 9.81334 
	rho=1.4
	g = param[0]
	r = param[1]
	return np.array([ h[1], -g + r * h[1]**2])

def drag_eqn(times,g,r):
	"""define scenario and integrate"""
	param = np.array([ g, r])
	hinit = np.array([0.0,0.0])       # initial values (position and velocity, respectively)
	h = odeint(deriv, hinit, times, args = (param,))
	return h[:,0], h[:,1]

def integral(times, YP, coeff_b):
	"""Returns arrays of h (height) and p (probability)"""

	#
	# load data into arrays
	#
	sigmas = [line.strip() for line in open('data/sigma_ds.dat')]
	alphas = [line.strip() for line in open('data/sigma_ds.dat')]
	drags  = [line.strip() for line in open('data/sigma_ds.dat')]

	#
	# convert to floats
	#
	sigma = map(float, sigmas)
	alpha = map(float, alphas)
	drag  = map(float, drags)


	# Initialize integral
	INTEGRAL = []
	for yp in YP:
		INTEGRAL.append(0.*yp)

	# Go over our MCMC samples
	g = 9.81334 
	samples = 1000
	for j in xrange(samples):
		MU = drag_eqn(times, g, coeff_b*drag[j])[0] + alpha[j]*times
		for yp, integral, mu in zip(YP, INTEGRAL, MU):
			tmp_int = scipy.stats.norm(mu, sigma[j]).pdf(yp)
			normfact = simps(tmp_int, yp)
			if normfact < 0.9:
				print j, mu, tmp_int
			assert normfact > 0.9, \
			'interval: Truncated too much; normfact = ' + str(normfact)
			integral += tmp_int / normfact

	for integral in INTEGRAL:
		integral /= samples


	return INTEGRAL 

# -------------------------------------------------------------
# Main Function
# -------------------------------------------------------------
#
# Stop module loading when imported.  Otherwise continue running.
import matplotlib.pyplot as plt

if __name__ == '__main__':

	times = np.linspace(0.,1600.,5)/600.
	g = 9.81334 
	rho=1.4
	rb =0.1166
	rbb=0.1066
	Mb =2.296
	Mbb=0.4548
	drag = 0.02

	coeff_b  = (rho*4*np.pi*rb**2.0)/(2.0*Mb)
	coeff_bb = (rho*4*np.pi*rbb**2.0)/(2.0*Mbb)        

	x, y = drag_eqn(times, g, coeff_b*drag)
	print x, y

	plt.plot(x, y)
#	plt.show()

	YP = []
	for xcoord in x:
		yp = np.linspace(xcoord-10, xcoord+10, 100)
		YP.append(yp)

	INTEGRAL = integral(times, YP, coeff_b)

	for yp, integral, xx in zip(YP, INTEGRAL, x):
		plotpdfandobs(yp, integral, xx)

#
# nick
# 5/4/14
#
