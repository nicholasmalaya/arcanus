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
import sys

#drag_fl = 'drag.dat'
#drag_fl = 'rankine.dat'
#drag_fl = 'constant.dat'
drag_fl = 'betz.dat'


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

# check grid is uniform
tol = 1e-3
if(np.abs(r[3] - r[2] - r[1]) > tol):
    print 'paradox: grid not uniform', r[3]-r[2]-r[1]
    print sys.exit(1)
    

h   = r[1]
c   = 0.4
rho = 1.225
b   = 6
omega = 10
rmax = 10.0
rmin = 1.0

vt_turb=omega*r

# vp=vt-vt_turb
vp = np.where(vt-vt_turb >= 0, vt-vt_turb, 0)
#for i in xrange(1,len(r)):
#    if(vp[i]<0):
#        vp[i]=0.0

U2 = ((vt)**2 + vz*vz)
U22 = ((vp)**2 + vz*vz)

#
# now, calculate angle phi
#
phi = np.where(vp != 0, vz/vp, np.pi/2.)
#np.arctan(vz/vp)
phi_deg = 360*phi/(2*np.pi)

# sanity check
if(len(phi_deg) != len(vt)):
    print 'paradox: inconsistent angles with velocities'
    print sys.exit(1)


#
# time to integrate
#

sm = 0.0
en = 0.0
for i in xrange(1,len(r)):
    if( rmin < r[i] < rmax ):
        sm += U22[i]*(cl(phi[i])*np.sin(phi[i]) + cd(phi[i])*np.cos(phi[i]))*r[i]
        sm += U22[i-1]*(cl(phi[i-1])*np.sin(phi[i-1]) + cd(phi[i-1])*np.cos(phi[i-1]))*r[i-1]
        en += vz[i]*(U2[i]) + vz[i-1]*(U2[i-1])

sm = sm*h/2.0
en = en*h/2.0

pt=sm*c*omega*b*rho/2./1000.
pa=np.pi*en*rho/2./1000.
#print 'Power Extracted by Turbine is ',sm*c*omega*b*rho/2., 'Watts'
print 'Power Extracted by Turbine is ',pt, ' kW'
print 'Power Available is ',pa, ' kW'
print 'Efficiency is, ', pt/pa
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
