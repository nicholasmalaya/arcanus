#
# create histogram from time series data
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as ss

dat=[]
tf = open('../src/beta.dat','r')
fig = plt.figure()
ax = fig.add_subplot(111)

for line in tf.readlines():
    keep = line
    dat.append(float(keep))

pdf, bins, patches = ax.hist(dat,25,normed=1,alpha=0.75,label="MCMC Histogram")

# add a line showing the expected distribution
alpha, beta=2.0, 5.0
rv = ss.beta(alpha,beta)
x = np.linspace(0,1) 
h = plt.plot(x, rv.pdf(x), lw=2,label='True Distribution')

# mean and average
mu = np.average(dat)
sigma = np.std(dat)

print mu, sigma

ax.set_xlabel(r'$x$')
ax.set_ylabel('Probability')
ax.grid(True)
plt.savefig("hist-beta.png")
plt.show()

#
# nick 
# 12/4/14
#
