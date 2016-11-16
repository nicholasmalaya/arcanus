#!/bin/py
#
# 
#
import sys

import numpy as np
#r = np.array([1.7,1.45,1.2,1.0])
#r = (r-r.min())/(r.max()-r.min())
#f = [0.54,0.32,0.20,0.28]
r = np.arange(1,0,-0.05)
f = [ 0.61405439,  0.53689096,  0.49637325, 0.46769237,  0.43770222, 0.39899252,
  0.35569226,  0.31518384,  0.29326381,  0.26199337,  0.25785942,  0.22897745,
  0.21421582,  0.18446327,  0.17814437,  0.16533107,  0.15043187,  0.1560824,
  0.16294177,  0.1585671]


test = [1,1,1,1]

fp = np.zeros(len(f))
rp = r[:len(r)-1]
for i in xrange(len(f)-1):
    fp[i] = ((f[i+1]-f[i])/(r[i+1]-r[i])/f[i]) + 1.5

print fp

#
# iteration number (should be same as flux, above)
#
#it = range(len(flux))

xmax=1.0
xmin=0.0

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

plt.plot(r,f, 'ko-', color='blue',label='Misfit')
plt.xlim(xmax, xmin)
#plt.ylim(0.9, 1.4)
plt.ylabel(r'$\frac{\langle {\bf u }\cdot {\bf n_v } \rangle}{||\, {\bf u}\, ||}$',
           fontsize=fsz,rotation=0,labelpad=40)
#ax.set_yscale('log')
plt.legend()
#ax.xaxis.set_major_formatter(plt.NullFormatter())


#
# figure two
#
plt.subplot(2,1,2)
plt.plot(r,fp, 'ko-', color='black',label='Logarithmic Derivative')
plt.ylabel(r'$\frac{f^{\prime}}{f}$',fontsize=fsz,rotation=0,labelpad=40)
plt.xlabel(r'$\frac{r-R_{m}}{R_{M}-R_{m}}$',fontsize=fsz)
plt.axhline(y=np.average(fp), linewidth=2, color = 'red',label='Average')
plt.xlim(xmax, xmin)
plt.legend(loc='best')


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
