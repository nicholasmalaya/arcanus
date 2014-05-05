#!/usr/bin/env python

import os
import numpy as np
import matplotlib.mlab as mlab
from scipy.integrate import simps

from read_data import read_data
from hpd import hpd, plotpdfandobs
from integral import integral


###############################################################################
# Get data (observations)

#DataFilesNames = ['Basket_Ball_1.dat', 'Basket_Ball_2.dat', 'Bowling_Ball_1.dat', 'Bowling_Ball_2.dat']
DataFilesNames = ['Basket_Ball_1.dat'] 

DataFolder = 'data/'
DataFiles = [DataFolder + name for name in DataFilesNames]

# Read all data points (+ clean-up suspicious ones)
allt, allh = [], []
for datafile in DataFiles:
	t, h = read_data(datafile)
	# remove last data points:
	allt.append(t[:-1])
	allh.append(h[:-1])


###############################################################################
# Compute posterior of observations at all points

samples = 100
yp, integrall = [], []
for tt in allt:
	yp_loc, int_loc = [], []
	for mytime in tt:
		my_yp, my_integral = integral(time) 
		yp_loc.append(my_yp)
		int_loc.append(my_integral)
	yp.append(yp_loc)
	integrall.append(int_loc)

# Final product should be
# yp, integrall
# where yp and integrall are multi-dimensional lists of same dimensions as allt + 1.
# I assume that the first two dimension are the same as allt.
# ie,
# yp[i][j] is the grid for the jth observation in the ith experiment
# and integrall[i][j] is the pdf for the jth obs in the ith exp.
# Test values:
#xtest = np.linspace(-40, 4, 100)
#pdftest = mlab.normpdf(xtest, 0, 1)
#pdftest = pdftest / simps(pdftest, xtest)
#yp, integrall = [], []
#for tt in allt:
#	locyp, locint = [], []
#	for ttt in tt:
#		locyp.append(xtest)
#		locint.append(pdftest)
#	yp.append(locyp)
#	integrall.append(locint)


###############################################################################
# Compute credibility intervals for each experiments:

beta = []
for x_L, pdf_L, obs_L in zip(yp, integrall, allh):
	beta_loc = []
	for x, pdf, obs in zip(x_L, pdf_L, obs_L):
		beta_loc.append( hpd(x, pdf, obs) )
	beta.append(beta_loc)


###############################################################################
# Plot posterior for obs along with obs for a few cases
# and save it to a file
Obs_ind = [5, 20, 35]
for beta_loc, filename, x_L, pdf_L, obs_L in zip(beta, DataFilesNames, yp, integrall, allh):
	justnameoffile, extension = os.path.splitext(filename)

	maxind = np.where(beta_loc == max(beta_loc))[0][0]
	x = x_L[maxind]
	pdf = pdf_L[maxind]
	obs = obs_L[maxind]
	plotpdfandobs(x, pdf, obs, justnameoffile + '_maxbeta', beta_loc[maxind]) 

	minind = np.where(beta_loc == min(beta_loc))[0][0]
	x = x_L[minind]
	pdf = pdf_L[minind]
	obs = obs_L[minind]
	plotpdfandobs(x, pdf, obs, justnameoffile + '_minbeta', beta_loc[minind])

	for myindex in Obs_ind:
		x = x_L[myindex]
		pdf = pdf_L[myindex]
		obs = obs_L[myindex]
		plotpdfandobs(x, pdf, obs, justnameoffile + '_' + str(myindex), beta_loc[myindex])

