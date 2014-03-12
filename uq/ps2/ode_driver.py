#!/bin/py
#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g  (object falling with no drag)
#
from scipy.integrate import odeint
import numpy as np
import pylab

def deriv(h,t): 
    """return derivatives of the array y"""
    g = 9.8                       # m/s/s
    b = 0.1
    return np.array([ h[1], -g + b * h[1]**2])

#
# define scenario
#
time = np.linspace(0.0,2.0,1000) # 10 seconds, divided into 10/1000 timesteps
hinit = np.array([0.0,0.0])       # initial values (position and velocity, respectively)
h = odeint(deriv,hinit,time)

#
# plot result of time integration
#
pylab.figure()
pylab.title("Scipy odeint example: Falling ball.")
pylab.plot(time,h[:,0], label='Position',color='black',linewidth=4) 
pylab.plot(time,h[:,1], label='Velocity',color='red', linestyle="dashed",linewidth=4) 
pylab.xlabel('Time (Seconds)',fontsize=15)
pylab.ylabel('Height (Meters)',fontsize=15)
pylab.rcParams['legend.loc'] = 'best'
pylab.legend()
pylab.show()

#
# nick 
# 3/4/13
#
