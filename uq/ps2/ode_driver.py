#!/bin/py
#
# Use scipy to integrate:
# 
#   dy^2 / dt^2 = -g + r (dh/dt)^2 (object falling with drag)
#
import pylab
import settings_infer
import numpy as np

#
# main function (example)
#
if __name__ == "__main__":
    """Example Driver for Solving Equation of Motion with Drag"""
    
    # ------------------------------
    # set params
    # ------------------------------
    g = 10.0
    r = 0.1

    # ------------------------------
    # solve at three times
    # ------------------------------
    times = np.array([0.0,1.0,2.0])
    pos1, vel1 = settings_infer.drag_eqn(times,g,r)

    # ------------------------------
    # solve at a series of times
    # ------------------------------
    times2 = np.linspace(0.0,2.0,1000)
    pos2, vel2 = settings_infer.drag_eqn(times2,g,r)

    # ------------------------------
    # plot result of time integration
    # ------------------------------
    pylab.figure()
    pylab.title("Scipy odeint example: Falling ball.")

    # plot first set
    pylab.plot(times,pos1, label='Position',color='black',linewidth=4) 
    pylab.plot(times,vel1, label='Velocity',color='red', linestyle="dashed",linewidth=4) 
    
    # plot second set
    pylab.plot(times2,pos2, label='Position',color='black',linewidth=4) 
    pylab.plot(times2,vel2, label='Velocity',color='red', linestyle="dashed",linewidth=4) 
    
    # labels
    pylab.xlabel('Time (Seconds)',fontsize=15)
    pylab.ylabel('Height (Meters)',fontsize=15)
    pylab.rcParams['legend.loc'] = 'best'
    pylab.legend()
    pylab.show()

#
# nick 
# 3/4/13
#
