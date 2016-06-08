#!/bin/py
#
# determine optimal energy from flow
#
#
#
# Radius VT  Vz
# m      m/s m/s
#
#
import numpy as np
import matplotlib.pyplot as plt

#drag_fl = 'drag.dat'
drag_fl = 'rankine.dat'


#
# first, import the data from drag.dat
#
ar_sz = sum(1 for line in open(drag_fl))
r  = np.empty(ar_sz)
vt = np.empty(ar_sz)
vz = np.empty(ar_sz)

f = open(drag_fl, 'r+')
it=0
for line in f:
    rr,vvt,vvz = line.split()
    r[it]  =rr
    vt[it] =vvt
    vz[it] =vvz
    it=it+1
f.close()

#
# now, 
#
phi = np.arctan(vz/vt)
print phi

#
# plot profiles
#

plt.plot(r,vt,'blue',label=r'$V_\theta$',linewidth=4)
plt.plot(r,vz,'r--',label=r'$V_z$',linewidth=4)
plt.xlabel('Radius (meters)')
plt.ylabel('Velocity (meters/sec)')
plt.grid(True)
plt.legend(loc='best')
# plt.xlim([0,360])
# plt.ylim([-2.1,2.1])
plt.savefig('profiles.png')

#
# nick
# 6/07/2016
#
