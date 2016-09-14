#!/bin/py
#
# 
#
import sys

# no twist
r = [1.7,1.45,1.2,1.0]
f = [0.54,0.32,0.20,0.28]

#
# iteration number (should be same as flux, above)
#
#it = range(len(flux))

xmax=1.8
xmin=1.0

#
# now, plot it and make it look good while you are at it
#
import numpy as np
import matplotlib.pyplot as plt
fsz=24

plt.figure(1)
plt.subplot(211)
#fig,ax = plt.subplots()


#
# figure one
#

plt.plot(r,f, 'ko-', color='blue',label='No Twist')
plt.xlim(xmax, xmin)
#plt.ylim(0.9, 1.4)
plt.ylabel(r'$\frac{\langle {\bf u }\cdot {\bf t_v } \rangle}{|| {\bf u} ||}$',fontsize=fsz,rotation=0,labelpad=40)
#ax.set_yscale('log')
plt.legend()
#ax.xaxis.set_major_formatter(plt.NullFormatter())


#
# figure two
#
plt.subplot(212)
plt.plot(r,f, 'ko-', color='blue',label='No Twist')
plt.ylabel(r'$\frac{f^{\prime}}{f}$',fontsize=fsz,rotation=0,labelpad=40)
plt.xlabel(r'Radius (meters)',fontsize=fsz)
plt.axhline(y=np.average(f), linewidth=2, color = 'red')
plt.xlim(xmax, xmin)

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
