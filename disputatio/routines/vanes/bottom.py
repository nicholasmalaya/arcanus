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
    t0=0; dt=0.05;
    r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
    for k in range(len(ic)):
        #
        # tEnd=np.sqrt(ic[k][0]**2 + ic[k][1]**2)-end
        #
        tEnd=radprime+0.2
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

    dom=10

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

    major_ticksx = np.arange(xmin, xmax, 5)
    minor_ticksx = np.arange(xmin, xmax, 1)                                         
    major_ticksy = np.arange(ymin, ymax, 5)
    minor_ticksy = np.arange(ymin, ymax, 1)                                         
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
    circleout=plt.Circle((0,0),R,color='black',linestyle='dotted',fill=False,linewidth=2)

    Rin = radmin
    circlein=plt.Circle((0,0),Rin,color='black',linestyle='dotted',fill=False,linewidth=2)

    # adding text
    ax.text(-9, 6, r'Upstream', fontsize=15)
    ax.text(5.4, 6, r'Downstream', fontsize=15)

    # angles
    ax.text(-6, -1, r'$\theta^{b,u}_{min}$', fontsize=20,color='blue')
    ax.text(6, -1, r'$\theta^{b,d}_{min}$', fontsize=20,color='blue')

    # annotate
    ax.annotate(r'$\theta^{b,u}_{max}$', xy=(-0.5, 0), xytext=(-6, -6),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)
    ax.annotate(r'$\theta^{b,d}_{max}$', xy=(0.5, 0), xytext=(6, -6),
                arrowprops=dict(facecolor='black', shrink=0.05),color='blue',fontsize=20)


    fig = plt.gcf()
    fig.gca().add_artist(circleout)
    fig.gca().add_artist(circlein)
    plt.axes().set_aspect('equal', 'datalim')

    plt.savefig('interp_entire_bottom.png',dpi=500)
    #plt.savefig('interp_entire_bottom.eps', format='eps', dpi=1000)

#
# EXECUTE
#
main()


#
# nick 
# 4/28/16 
#
