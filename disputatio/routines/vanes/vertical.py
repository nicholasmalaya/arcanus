#!/bin/py
#
# interpolate over data field for bottom vanes
#
#
#
import numpy as np
import matplotlib
matplotlib.use('Agg')
import itertools
import matplotlib.pyplot as plt

from scipy import integrate
from scipy.integrate import ode

radprime=6.0
radmin=0.6


#
# main function: execute
#
def main():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    dom=10

    xmin = -dom
    xmax = dom

    zmin = -dom
    zmax = dom
    
    plt.suptitle("SoV Configuration: Side View")
    plt.title("12 Vane")

    major_ticksx = np.arange(xmin, xmax, 5)
    minor_ticksx = np.arange(xmin, xmax, 1)                                         
    major_ticksy = np.arange(zmin, zmax, 5)
    minor_ticksy = np.arange(zmin, zmax, 1)                                         
    ax.set_xticks(major_ticksx)
    ax.set_xticks(minor_ticksx, minor=True) 
    ax.set_yticks(major_ticksz)
    ax.set_yticks(minor_ticksz, minor=True)

    plt.xlim([xmin,xmax])
    plt.ylim([zmin,zmax])
    plt.xlabel('Streamwise (X) [Meters]')
    plt.ylabel('Height (Z) [Meters]')
    plt.grid()

    # adding text
    ax.text(-8.4, 6, r'Upstream Side', fontsize=15)
    ax.text(5.6, 6, r'Downstream Side', fontsize=15)

    # angles
    ax.text(-8, -1, r'$\theta^{b,u}_{min}$', fontsize=20,color='blue')
    ax.text(6, -1, r'$\theta^{b,d}_{min}$', fontsize=20,color='blue')

    # annotate
    ax.annotate(r'$\theta^{b,u}_{max}$', xy=(-0.5, 0), xytext=(-6, -6),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)
    ax.annotate(r'$\theta^{b,d}_{max}$', xy=(0.5, 0), xytext=(6, -6),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)

    # outer and inner radius
    ax.annotate(r'$r^{b}_{max}$', xy=(-4.6, 4), xytext=(-9, 2),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)
    


    fig = plt.gcf()
    fig.gca().add_artist(circleout)
    fig.gca().add_artist(circlein)
    plt.axes().set_aspect('equal', 'datalim')

    plt.savefig('interp_entire_bottom.png',dpi=500)
    plt.savefig('interp_entire_bottom.pdf', format='pdf', dpi=1000)

#
# EXECUTE
#
main()


#
# nick 
# 4/28/16 
#
