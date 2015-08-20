#!/bin/py
#
# lets plot the kinetic energy against
# the derived gravitational potential energy
#
import numpy as np
import matplotlib.pyplot as plt

#
# parameters (see document)
#
rho    = 1.225 # [Kg/m^3]
u      = 5.0   # [m/s]
R      = 3.0   # [m]
delta  = 0.10  # [m]
#
dt     = 30.0  # [Kelvin]
T      = 313   # [Kelvin]
beta   = 1/T   # [1/Kelvin]
g      = 9.8   # [m/s^2]

#
# arrays 
#
h  = np.linspace(0.0, 100.0)
ke = R*rho*u**3 * (h - 10*delta/11.)
pe = u*beta*rho*dt*g*(h**3/3.0 - 7*delta**3/30.)

# plot it
plt.plot(h,ke,'blue',label='Kinetic Energy')
plt.plot(h,pe,'red',label='Gravitational Potential Energy')
plt.set_xlabel('Height')
plt.set_ylabel('Energy')
plt.grid(True)
plt.save_fig('cross.png')
#plt.show()


#
# nick
# 8/19/2015
#
