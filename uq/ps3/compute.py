#!/usr/bin/env python

import os
import numpy as np
import matplotlib.mlab as mlab
from scipy.integrate import simps

from read_data import read_data
from hpd import hpd, plotpdfandobs
from integral_alt import integral


###############################################################################
# Get data (observations)

#DataFilesNames = ['Basket_Ball_1.dat', 'Basket_Ball_2.dat', 'Bowling_Ball_1.dat', 'Bowling_Ball_2.dat']
DataFilesNames = ['Basket_Ball_1.dat'] 

DataFolder = 'data/'
DataFiles = [DataFolder + name for name in DataFilesNames]

# Read all data points (+ clean-up suspicious ones)
Dx = 5.0
gridpts = 1000

allt, allh, allYP = [], [], []
for datafile in DataFiles:
	YP = []
	t, h = read_data(datafile)
	t = np.array(t[:-1])/600.
	h = h[:-1]
	# Assemble YP:
	for hh in h:
		YP.append(np.linspace(hh-Dx, hh+Dx, gridpts))
	# remove last data points:
	allt.append(t)
	allh.append(h)
	allYP.append(YP)

###############################################################################
# Compute posterior of observations at all points

allINTEGRAL = []

rho = 1.4
rb = 0.1166
rbb = 0.1066
Mb = 2.296
Mbb = 0.4548

coeff_b = (rho*4*np.pi*rb**2.0)/(2.0*Mb)
coeff_bb = (rho*4*np.pi*rbb**2.0)/(2.0*Mbb)        

for times, YP, filename in zip(allt, allYP, DataFilesNames):
	if 'Basket' in filename:
		INTEGRAL = integral(times, YP, coeff_b)
	else:
		INTEGRAL = integral(times, YP, coeff_bb)
	allINTEGRAL.append(INTEGRAL)

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
# Compute credibility intervals for each experiment:

beta = []
for x_L, pdf_L, obs_L in zip(allYP, allINTEGRAL, allh):
	beta_loc = []
	for x, pdf, obs in zip(x_L, pdf_L, obs_L):
		beta_loc.append( hpd(x, pdf, obs) )
	beta.append(beta_loc)


###############################################################################
# Plot posterior for obs along with obs for a few cases
# and save it to a file
Obs_ind = [5, 20, 35]
for beta_loc, filename, x_L, pdf_L, obs_L in zip(beta, DataFilesNames, allYP, allINTEGRAL, allh):
	justnameoffile, extension = os.path.splitext(filename)

	maxind = np.where(beta_loc == max(beta_loc))[0][0]
	x = x_L[maxind]
	pdf = pdf_L[maxind]
	obs = obs_L[maxind]
	plotpdfandobs(x, pdf, obs, justnameoffile + '_maxbeta' + str(maxind), beta_loc[maxind]) 

	minind = np.where(beta_loc == min(beta_loc))[0][0]
	x = x_L[minind]
	pdf = pdf_L[minind]
	obs = obs_L[minind]
	plotpdfandobs(x, pdf, obs, justnameoffile + '_minbeta' + str(minind), beta_loc[minind])

	for myindex in Obs_ind:
		x = x_L[myindex]
		pdf = pdf_L[myindex]
		obs = obs_L[myindex]
		plotpdfandobs(x, pdf, obs, justnameoffile + '_' + str(myindex), beta_loc[myindex])


###############################################################################
# Save beta's to file
outp = open('betas.out', 'w')

for filename, beta_loc in zip(DataFilesNames, beta):
	outp.write(' %s: \n' % filename)
	for betai in beta_loc:
		outp.write(' %14.6e\n' % betai)
	outp.write('\n\n')
