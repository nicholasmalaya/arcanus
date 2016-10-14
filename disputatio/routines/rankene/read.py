# "T","u","v","w","p","k","mu",
# "vel_penalty_:0","vel_penalty_:1","vel_penalty_:2",
# "vel_source_:0","vel_source_:1","vel_source_:2",
# "Points:0","Points:1","Points:2"

#
# read CSV and import into plot
# 14,15,16

import csv

ifile  = open('lower.csv', "rb")

# stupid initialization of list
T = []
u = []
v = []
w = []
x = []

csvReader1 = csv.reader(ifile)
for row in csvReader1:
    T.append(row[0])
    u.append(row[1])
    v.append(row[2])
    w.append(row[3])
    x.append(row[13])
    y      = row[14]
    height = row[15] 

ifile.close()

import numpy as np

u_vel = np.array(u, dtype=float)
v_vel = np.array(v, dtype=float)

theta = np.sqrt(u_vel*u_vel+v_vel*v_vel)

#
# get max, etc.
#
u_vel=u_vel/u_vel.max()
u_max = u_vel.argmax()

x = np.array(x, dtype=float)
x = x-0.65

x_max = x[u_max]+.02
print x_max
x = x/x_max

#
# plot
#
import matplotlib.pyplot as plt

# plt.plot(x, y)

r = [0,.103,.22,.46,.58,.85,.95,1.18,1.3,1.57,1.68,1.93,2.0,2.3,2.4,2.6,2.78,3.0,3.1,3.4,3.5,3.7,3.85,4.12,4.49,4.8,5.0]

uu = [0,.0936,0.19,.55,.74,.96,1.0,.94,.87,.68,.61,.42,0.37,.25,.23,.11,.055,.108,.093,.03,-0.01,.02,.06,.086,.11,.17,.2]

from scipy.interpolate import interp1d

x_smooth = np.linspace(0, 5, 200)
f2 = interp1d(r, uu, kind=4)

#plt.plot(x,np.abs(u_vel),'o', label='Simulation')
#plt.plot(r,uu,'-', label='Simulation',linewidth=3)

plt.plot(x_smooth,f2(x_smooth),'--', label='Simulation',linewidth=3)

#plt.ylim([0,3])
plt.xlim([0,5])


linear = np.linspace(0.0, 1.0, num=5)
plt.plot(linear,linear,label='Rankene Vortex Model' ,color='black',linewidth=3)

overrx = np.linspace(1.0, 5.0, num=50)
overr =  1/(overrx)**1.5
plt.plot(overrx,overr ,color='black',linewidth=3)

#
#
fsz=20
plt.ylabel(r'$u_{\theta}/u^{Max}_{\theta}$',fontsize=fsz,rotation="0",labelpad=20)
plt.xlabel(r'$r/r^{Max}$',fontsize=fsz)
plt.legend(loc='best')
plt.axes().set_aspect('equal', 'datalim')



#plt.show()
plt.tight_layout()
plt.savefig('rankene.png')

#
# https://en.wikipedia.org/wiki/Rankine_vortex
#

#
# nick
#
