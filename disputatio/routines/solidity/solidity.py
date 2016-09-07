#!/bin/py
#
# 
#
import sys

# no solidity
flux = [1.11,1.44,1.83,2.10]
it = [2,4,6,8]

# solidity
flux2 = [1.05,.852,0.012,0]
it2 = [2,4,6,8]
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
plt.plot(it,flux, 'ko-', color='blue',label='No Solidity Model')
plt.plot(it2,flux2, 'ko--', color='red',label='Solidity Model')

plt.xlim(0, 10)
plt.ylim(0, 2.2)
plt.ylabel(r'Turbine Power Extracted (kW)',fontsize=fsz)
plt.xlabel(r'# of Blades',fontsize=fsz)
#ax.set_yscale('log')
plt.legend(loc='best')
#ax.xaxis.set_major_formatter(plt.NullFormatter())

#
# save figure
#
plt.savefig('solidity.png')

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
# 9/7/16
#
