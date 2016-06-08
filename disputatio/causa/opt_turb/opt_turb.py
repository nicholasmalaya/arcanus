#!/bin/py
#
# determine optimal energy from flow
#
#
def cl(phi):
    if(phi>180):
        cl = -1.75
    else:
        cl = 1.75
    return cl

def cd(phi):
    if(270>phi>180):
        cd = 0
    else:
        cd = 2.0
    return cd

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

U2 = (vt*vt+vz*vz)

#
# now, calculate angle phi
#
phi = np.arctan(vz/vt)
phi_deg = 360*phi/(2*np.pi)

# sanity check
if(len(phi_deg) != len(vt)):
    print 'paradox: inconsistent angles with velocities'
    print sys.exit(1)


#
# time to integrate
#



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
