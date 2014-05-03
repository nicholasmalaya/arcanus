#
#
#

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.integrate import simps
from copy import copy


def hpd(x, pdf, obs):
	"""	Compute credibility interval (beta) """

	assert (abs(simps(pdf,x) - 1.0) < 1e-12) , 'hpd(x, pdf, obs): pdf must integrate to 1'
	assert (x[0] < obs) and (obs < x[-1]), 'hpd(x, pdf, obs): obs must be contained in x'

	pobs = np.interp(obs, x, pdf)

	pdfc = copy(pdf)
	pdfc[np.where(pdfc < pobs)] = 0
	
	# For debugging only:
#	plt.figure()
#	plt.plot(x, pdfc, 'o-')    
#	plt.title('in hpd()')
#	plt.show()

	beta = simps(pdfc, x)

	return beta


#
# main function
# 
if __name__ == '__main__':
	mean = 0
	variance = 1
	sigma = np.sqrt(variance)
	x     = np.linspace(-3,3,100)
	pdf   = mlab.normpdf(x,-1,0.5) + mlab.normpdf(x, 1, 0.5)
	pdf = pdf / simps(pdf, x)
#	print pdf
	plt.figure()
	plt.plot(x,pdf, 'o-')    
	plt.title('Before hpd()')
	plt.show()

	beta = hpd(x, pdf, 0.5) 
	print beta
