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

radprime=3.0
radmin=0.6

def vf(t,x):
    #
    # Vector field function
    #
    thetabs_f = 80*np.pi/180.0 # moving from 70 to 80
    thetabs_b = 50*np.pi/180.0 # moving from 70 to 80

    rb  = radmin
    rmb = radprime-0.1

    r     = np.sqrt(x[0]**2 + x[1]**2)
    theta = np.arctan2(x[1],x[0])

    if(x[0]>0):
        thetab = -(thetabs_f)*np.power(np.abs((r-rb)/(rmb-rb)),0.5)+thetabs_f
    else:
        thetab = -(thetabs_b)*np.power(np.abs((r-rb)/(rmb-rb)),1.2)+thetabs_b

    thetabb = theta + thetab

    dx=np.zeros(2)
    dx[0]=-np.cos(thetabb)
    dx[1]=-np.sin(thetabb)

    return dx

def arr():
    #
    # Solution curves
    #
    #rad = 0.4
    rad = radprime-0.1
    theta = np.linspace(0, 2*np.pi, 13)
    ic    = np.stack((rad*np.cos(theta),rad*np.sin(theta)),axis=-1)

    end = 0.0
    t0=0; dt=0.01;
    r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
    for k in range(len(ic)):
        #
        # tEnd=np.sqrt(ic[k][0]**2 + ic[k][1]**2)-end
        #
        tEnd=radprime+0.0
        Y=[];T=[];S=[];
        r.set_initial_value(ic[k], t0)
        while r.successful() and r.t +dt < tEnd:
            r.integrate(r.t+dt)
            Y.append(r.y)

        S=np.array(np.real(Y))
        plt.plot(S[:,0],S[:,1], color = 'red', lw = 4.25)




#
# main function: execute
#
def main():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    dom=5

    xmin = -dom
    xmax = dom

    ymin = -dom
    ymax = dom
    
    #
    # Evaluate it on a grid...
    #
    nx, ny = 200, 200
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, nx), 
                         np.linspace(ymin, ymax, ny))

    #
    # m is a matrix of polynomial values...
    # e.g. 

    #
    # Plot!
    #
    arr()
    # 
    # ----------------------------------------
    
    plt.suptitle("SoV Configuration: Bottom Tier")
    plt.title("12 Vane")

    major_ticksx = np.arange(xmin, xmax, 1)
    minor_ticksx = np.arange(xmin, xmax, 0.1)                                         
    major_ticksy = np.arange(ymin, ymax, 1)
    minor_ticksy = np.arange(ymin, ymax, .1)                                         
    ax.set_xticks(major_ticksx)
    ax.set_xticks(minor_ticksx, minor=True) 
    ax.set_yticks(major_ticksy)
    ax.set_yticks(minor_ticksy, minor=True)

    plt.xlim([xmin,xmax])
    plt.ylim([ymin,ymax])
    plt.xlabel('Streamwise (X) [Meters]')
    plt.ylabel('Spanwise (Y) [Meters]')
    plt.grid()

    # add circle(s)
    R = radprime
    circleout=plt.Circle((0,0),R,color='black',linestyle='dashed',fill=False,linewidth=2)

    Rin = radmin
    circlein=plt.Circle((0,0),Rin,color='black',linestyle='dashed',fill=False,linewidth=1)

    # adding text
    ax.text(-4.4, radprime, r'Upstream Side', fontsize=15)
    ax.text(2.6, radprime, r'Downstream Side', fontsize=15)

    # angles
    ax.text(-3.9, 0, r'$\phi^{b,u}$', fontsize=20,color='blue')
    ax.text(3.2, 0, r'$\phi^{b,d}$', fontsize=20,color='blue')

    # annotate
    ax.annotate(r'$\theta^{b,u}$', xy=(-0.2, 0), xytext=(-radprime, -radprime),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)
    ax.annotate(r'$\theta^{b,d}$', xy=(0.2, 0), xytext=(radprime, -radprime),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)

    # outer and inner radius
    ax.annotate(r'$r^{b}_{max}$', xy=(-3.1, 0), xytext=(0.2, .15),
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
