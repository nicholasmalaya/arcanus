#!/bin/py
#
# 
#
import sys

#
# list of our fluxes
# 686 august field test simulations
# 796 optimized axisymmetric vanes
# 803 watts is back cylinder 
# 930 is cylinder back with optimized linear vanes
# 1102 elliptic vanes
# 1380 optimized elliptic vanes
# 2203 horizontal partitions
flux = [686,796,803,930,1102,1380,2203,3058,2850]

#
# iteration number (should be same as flux, above)
#
it = range(len(flux))

#
# notes on each run
#
nts = ['Field Test',
        'Curved vanes',
        'Cylinder',
        'Linear curvature',
        'Elliptic Vanes',
        'Optimized Elliptic',
        'Horizontal Partitions',
        'Asymmetric 1st Tier',
        'Turbine']

# nts = ['Straight Vanes',
#        '',
#        '',
#        'Kick-up Ramps',
#        '',
#        'Optimized Kick-up Forcing',
#        'Optimization Vane Curvature',
#        'Optimization Vane Angle',
#        'Cone',
#        'Present']

if( len(nts) != len(flux)):
    print 'Paradox! Notes must be present for each case!'
    sys.exit(1)

#
# now, plot it and make it look good while you are at it
#
import matplotlib.pyplot as plt
fsz=32

#plt.subplot(1, 1, 1)
fig,ax = plt.subplots()
plt.plot(it,flux, 'ko-', color='blue')
plt.xlim(-0.7, it[-1]+0.5)
plt.ylim(600, 3200)
plt.ylabel(r'Kinetic Energy Flux (W)',fontsize=fsz)
plt.xlabel(r'Optimization Case',fontsize=fsz)
#ax.set_yscale('log')

ax.xaxis.set_major_formatter(plt.NullFormatter())


#i=0
for i in xrange(len(nts)):
    ax.annotate(nts[i], xy=(it[i],flux[i]), xytext=(20, 30),
                textcoords = 'offset points', ha = 'right', va = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

#
# save figure
#
plt.savefig('flux_opt_wind.png')

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
