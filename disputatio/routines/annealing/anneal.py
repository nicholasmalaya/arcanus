#!/bin/py
#
# 
#
import sys

# no twist
flux = [0.99,1.02,1.06,1.1,1.09,1.11,1.117,1.12,1.115,1.10,1.04]
it = [35,40,43,45,47,50,53,55,57,60,65]

# twist
flux2 = [1.13,1.25,1.32,1.33,1.34,1.33,1.31,1.25]
it2 = [35,40,43,45,47,49,50,55]
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
plt.plot(it,flux, 'ko-', color='blue',label='No Twist')
plt.plot(it2,flux2, 'ko-', color='red',label='With Twist')

#plt.axvline(x=55,linewidth=2, color = 'blue')
#plt.axvline(x=47, ymin=0.5, ymax = 1.1, linewidth=2, color = 'red')

plt.xlim(30, 70)
plt.ylim(0.9, 1.4)
plt.ylabel(r'Turbine Power Extracted (kW)',fontsize=fsz)
plt.xlabel(r'Collective (degrees)',fontsize=fsz)
#ax.set_yscale('log')
plt.legend()
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
