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

    dom=15

    xmin = -dom
    xmax = dom

    zmin = 0
    zmax = 7
    
    plt.title("SoV Configuration: Vertical View")
    #plt.title("12 Vane")

    major_ticksx = np.arange(xmin, xmax, 5)
    minor_ticksx = np.arange(xmin, xmax, 1)                                         
    major_ticksz = np.arange(zmin, zmax, 5)
    minor_ticksz = np.arange(zmin, zmax, 1)                                         
    ax.set_xticks(major_ticksx)
    ax.set_xticks(minor_ticksx, minor=True) 
    ax.set_yticks(major_ticksz)
    ax.set_yticks(minor_ticksz, minor=True)

    plt.xlim([xmin,xmax])
    plt.ylim([zmin,zmax])
    plt.xlabel('Streamwise (X) [Meters]')
    plt.ylabel('Height (Z) [Meters]')
    plt.grid()

    # adding lines
    #plt.axhline(y=3.0, xmin=-12.0, xmax=0, linewidth=4, color = 'red')

    # front vane
    plt.plot((-12,-3),(3,3),linewidth=4,color = 'red')

    # back vane (x1,x2),(y1,y2)
    
    # front vane (top tier)
    plt.plot((-12,-3),(3,3),linewidth=4,color = 'red')
    plt.plot((-12,-12),(3,0.5),linewidth=4,color = 'red')
    plt.plot((-12,-3),(0.5,0.5),linewidth=4,color = 'red')
    plt.plot((-12,-3),(0.5,0.5),linewidth=4,color = 'red')
    plt.plot((-3,-3),(3,0.5),linewidth=4,color = 'red')

    # back cyl
    plt.plot((3,3),(1,3),linewidth=4,color = 'red')

    # bottom tier front
    plt.plot((-0.6,-0.6),(0,0.5),linewidth=4,color = 'red')
    plt.plot((-6,-6),(0,0.5),linewidth=4,color = 'red')
    plt.plot((-0.6,-6),(0,0),linewidth=4,color = 'red')
    plt.plot((-0.6,-6),(0.5,0.5),linewidth=4,color = 'red')

    # bottom tier back
    plt.plot((0.6,0.6),(0,1),linewidth=4,color = 'red')
    plt.plot((6,6),(0,1),linewidth=4,color = 'red')
    plt.plot((0.6,6),(1,1),linewidth=4,color = 'red')

    # adding text
    ax.text(-13, 5, r'Upstream Side', fontsize=15)
    ax.text(5.6, 5, r'Downstream Side', fontsize=15)

    # cone (front, then back)
    plt.plot((3,1.5),(3,5),linewidth=4,color = 'red')
    plt.plot((-3,-1.5),(3,5),linewidth=4,color = 'red')

    # angles
    #ax.text(-8, -1, r'$\theta^{b,u}_{min}$', fontsize=20,color='blue')
    #ax.text(6, -1, r'$\theta^{b,d}_{min}$', fontsize=20,color='blue')

    # annotate
    #ax.annotate(r'$\theta^{b,u}_{max}$', xy=(-0.5, 0), xytext=(-6, -6),
    #            arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)

    #
    # 
    # 
    #ax.annotate(r'$L_{x}$', xy=(-12,2),xytext=(0, 2),
    #            arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=10,size=10)
    #ax.annotate(r'$r^{cyl}$', xy=(3,2), xytext=(0, 2),
    #            arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=5)

    ax.annotate('$L_{x}$', xy=(-12, 2), xycoords='data',
                xytext=(0, 1.7), textcoords='data',
                arrowprops=dict(arrowstyle="->"), color='blue'
            )

    ax.annotate('$H^t$', xy=(-5, 3), xycoords='data',
                xytext=(-5.5, 0), textcoords='data',
                arrowprops=dict(arrowstyle="->"), color='blue'
            )

    fig = plt.gcf()
    plt.axes().set_aspect('equal')

    plt.savefig('vertical_design.png',dpi=500)
    plt.savefig('vertical_design.pdf', format='pdf', dpi=1000)

#
# EXECUTE
#
main()


#
# nick 
# 4/28/16 
#
