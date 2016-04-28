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

#
# adding functions
#
## thetab  := -(thetabs_f)*pow(abs((r-(rb-0.3))/((rmb-rb-0.3))),0.4)+thetabs_f
## thetabb := -(thetabs_b)*pow(abs((r-(rb-0.3))/((rmb-rb-0.3))),0.4)+thetabs_b
## thetab  := (${Physics/VelocityPenalty/thetabs_f}/(${Physics/VelocityPenalty/rmb}-(${Physics/VelocityPenalty/rb}-0.3)))*((${Physics/VelocityPenalty/rb}-0.3)-r);


def vf(t,x):
    #
    # Vector field function
    #
    thetabs_f = 80*np.pi/180.0 # moving from 70 to 80
    thetabs_b = 50*np.pi/180.0 # moving from 70 to 80

    rb  = 0.3
    rmb = 3.0

    r = np.sqrt(x[0]**2 + x[1]**2)

    if(x[0]>0):
        theta = -(thetabs_f)*np.power(np.abs((r-rb)/(rmb-rb)),0.5)+thetabs_f
    else:
        theta = -(thetabs_b)*np.power(np.abs((r-rb)/(rmb-rb)),1.2)+thetabs_b


    dx=np.zeros(2)
    dx[0]=np.cos(theta)
    dx[1]=np.sin(theta)

    return dx

def arr():
    #
    # Solution curves
    #
    h = 1
    ic=[[h,-4]]
    end = 0.0
    t0=0; dt=0.1;
    r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
    for k in range(len(ic)):
        tEnd=np.sqrt(ic[k][0]**2 + ic[k][1]**2)-end
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


    xmin = -10
    xmax = 10

    ymin = -10
    ymax = 10
    
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

    # add circle
    R = 3.0
    circleout=plt.Circle((0,0),R,color='black',linestyle='dotted',fill=False,linewidth=4)

    Rin = 0.3
    circlein=plt.Circle((0,0),Rin,color='black',linestyle='dotted',fill=False,linewidth=4)

    fig = plt.gcf()
    fig.gca().add_artist(circleout)
    fig.gca().add_artist(circlein)
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('interp_entire_top.png')

#
# EXECUTE
#
main()


#
# nick 
# 4/28/16 
#
