#!/bin/py
#
# 
#
import sys
import numpy as np

# no twist
flux = 1.35* np.array([0.99,1.02,1.1,1.12,1.12,1.11,1.112,1.123,1.1159,1.101,1.042])
it = [35,40,43,45,47,50,53,55,57,60,65]

#
# duane (top)
#
fluxd = 1.45*np.array([0.99,1.02,1.06,1.1,1.09,1.11,1.117,1.12,1.115,1.10,1.04])
itd = [35,40,43,45,47,50,53,55,57,60,65]

#
# twist
#
flux2 = 1.6*np.array([1.13,1.25,1.32,1.33,1.34,1.33,1.31,1.25,1.11,1.125,1.15])
it2 = [35,40,43,45,47,50,53,55,57,60,65]

flux2d = 1.7*np.array([1.02,1.2,1.321,1.335,1.335,1.325,1.29,1.22,1.11])
it2d = [35,40,43,45,47,50,53,55,57]


print np.max(flux2)
print np.max(flux)
#
# iteration number (should be same as flux, above)
#
#it = range(len(flux))

#
# now, plot it and make it look good while you are at it
#
import matplotlib.pyplot as plt
fsz=24

#plt.subplot(1, 1, 1)
fig,ax = plt.subplots()
plt.plot(it,flux, 'kd--', color='blue',label='CFD with no Twist')
plt.plot(itd,fluxd, 'kd-', color='blue',label='Frozen with no Twist')

plt.plot(it2,flux2, 'ko--', color='red',label='CFD with Twist')
plt.plot(it2d,flux2d, 'ko-', color='red',label='Frozen with Twist')

#plt.axvline(x=55,linewidth=2, color = 'blue')
#plt.axvline(x=47, ymin=0.5, ymax = 1.1, linewidth=2, color = 'red')

plt.xlim(30, 80)
plt.ylim(1.2, 2.5)
plt.ylabel(r'Turbine Power Extracted (kW)',fontsize=fsz)
plt.xlabel(r'Inner Blade Angle (degrees)',fontsize=fsz)
#ax.set_yscale('log')
plt.legend(loc='best')
#ax.xaxis.set_major_formatter(plt.NullFormatter())

#
# save figure
#
plt.savefig('collective.png')

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
