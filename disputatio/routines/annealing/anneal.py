#!/bin/py
#
# 
#
import sys

import numpy as np
r = [1.7,1.45,1.2,1.0]
f = [0.54,0.32,0.20,0.28]
test = [1,1,1,1]

fp = np.zeros(len(f))
rp = r[:len(r)-1]
for i in xrange(len(f)-1):
    fp[i] = (f[i+1]-f[i])/(r[i+1]-r[i])

print fp

#
# iteration number (should be same as flux, above)
#
#it = range(len(flux))

xmax=1.8
xmin=1.0

#
# now, plot it and make it look good while you are at it
#
import matplotlib.pyplot as plt
fsz=24

plt.subplot(2,1,1)
#fig,ax = plt.subplots()

#
# figure one
#

plt.plot(r,f, 'ko-', color='blue',label='No Twist')
plt.xlim(xmax, xmin)
#plt.ylim(0.9, 1.4)
plt.ylabel(r'$\frac{\langle {\bf u }\cdot {\bf t_v } \rangle}{||\, {\bf u}\, ||}$',fontsize=fsz,rotation=0,labelpad=40)
#ax.set_yscale('log')
plt.legend()
#ax.xaxis.set_major_formatter(plt.NullFormatter())


#
# figure two
#
plt.subplot(2,1,2)
plt.plot(r,fp, 'ko-', color='blue',label='Log Derivative')
plt.ylabel(r'$\frac{f^{\prime}}{f}$',fontsize=fsz,rotation=0,labelpad=40)
plt.xlabel(r'$\frac{r-R_{m}}{R_{M}-R_{m}}$',fontsize=fsz)
plt.axhline(y=np.average(fp), linewidth=2, color = 'red')
plt.xlim(xmax, xmin)
plt.legend()

#
# save figure
#
plt.tight_layout()
plt.savefig('annealing.png')

#
# MARK IT ZERO
#

print 'exiting successfully...'
sys.exit(0)

#
# invoked from command line as:
#
# python plot_flux.py
#

#
# nick 
# 2/26/15
#
