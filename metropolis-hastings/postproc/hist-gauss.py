#
# create histogram from time series data
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

dat=[]
tf = open('../src/gauss.dat','r')
fig = plt.figure()
ax = fig.add_subplot(111)

for line in tf.readlines():
    keep = line
    dat.append(float(keep))

pdf, bins, patches = ax.hist(dat,25,normed=1,alpha=0.75,label="MCMC Histogram")

mean  = -10
sigma = 1.0
x = np.linspace(-14,-6,100)
plt.plot(x,mlab.normpdf(x,mean,sigma),linewidth=2, color='r',label='True Distribution')
plt.legend()

# add a line showing the expected distribution
mu = np.average(dat)
sigma = np.std(dat)

print mu, sigma

ax.set_xlabel(r'$\mu$')
ax.set_ylabel('Probability')
ax.grid(True)
plt.savefig("hist-gauss.png")
plt.show()

#
# nick 
# 12/4/14
#
