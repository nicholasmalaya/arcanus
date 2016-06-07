#!/bin/py
#
# lets plot the kinetic energy against
# the derived gravitational potential energy
#
import numpy as np
import matplotlib.pyplot as plt

#
# arrays 
#
h  = np.linspace(0.0, 360.0)
cl = 1.75*np.ones(len(h))
cd = np.zeros(len(h))

#
#
cl[len(h)/2:]=-1.75
cd[:len(h)/4]=2.0
cd[3*len(h)/4:]=2.0
# plot it
plt.plot(h,cl,'blue',label=r'$C_L$',linewidth=4)
plt.plot(h,cd,'r--',label=r'$C_D$',linewidth=4)
plt.xlabel('Degrees')
plt.ylabel('Coefficient of Lift/Drag')
plt.grid(True)
plt.legend(loc='best')
plt.xlim([0,360])
plt.ylim([-2.1,2.1])
plt.savefig('drags.png')
#plt.show()


#
# nick
# 6/07/2016
#
