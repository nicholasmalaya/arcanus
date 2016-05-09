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
flux = [180,435,688,705,843,940,1320,1510,1800]

#
# iteration number (should be same as flux, above)
#
it = range(len(flux))

#
# notes on each run
#
nts = ['Initial Guess','Half Cylinder Drag Polars','Blade Angle Opt','Center Gap','Blade # Opt','Linear Twist','Semicircles','Cone Opt','Doubled horizontal']

# drag polars,twist

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
plt.xlim(-1.7, it[-1]+0.5)
plt.ylim(0, 2200)
plt.ylabel(r'Kinetic Energy Flux (W)',fontsize=fsz)
plt.xlabel(r'Optimization Case',fontsize=fsz)
#ax.set_yscale('log')

ax.xaxis.set_major_formatter(plt.NullFormatter())


#i=0
# textcoords = 'offset points'
for i in xrange(len(nts)):
    ax.annotate(nts[i], xy=(it[i],flux[i]), xytext=(10, 40+min(i*15,40)),
                textcoords = 'offset points', 
                ha = 'right', va = 'top',
                bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.7),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

#
# save figure
#
plt.savefig('turbine_opt.png')

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
