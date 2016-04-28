#!/bin/py
#
# interpolate over data field with 2d polynomial fit
#
#  fit a 2D, 3rd order polynomial to data
#  estimate the 16 coefficients using all of your data points.
#
# http://stackoverflow.com/questions/18832763/drawing-directions-fields
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
import top

hprime = -12
Rprime = 3.0
def load_ell():
    #
    # Generate Data from ellipses
    #
    h           = hprime
    thetaf      = 20*np.pi/180.
    a           = -h*1.0
    miny        = -1

    #
    # create data
    # 
    space   = 0.02
    R       = Rprime
    y0      = np.arange(Rprime,miny,-space)

    x0      = -np.sqrt(R*R-y0*y0)
    theta0  = np.arctan2(y0,x0)
    
    thetafy = thetaf*(R-y0)/R
    #thetafy = thetaf*np.arccos(y0/R)/2.

    thetam = theta0-np.pi/2-thetafy

    m       = np.tan(thetam)
    k       = (y0 + a*a*m/(x0-h) - m*(x0-h))
    bs      = -a*a*m*(y0-k)/(x0-h)
    b       = np.sqrt(bs)

    xl = []
    yl = []
    zl = []

    print 'y0 ', y0
    print 'b/a: ',b/a

    fudge = 0.05
    dx_space=0.1
    for i in xrange(len(k)):
        dx = np.arange(h,x0[i]+fudge,dx_space)
        xl = xl + dx.tolist()

        dy = -(b[i]*np.sqrt(1-((dx-h)/(a))**2))+k[i]
        #yl.append(-(b[i]*np.sqrt(1-((dx-h)/(a))**2))+k[i])
        yl = yl + dy.tolist()

        #zl.append(np.arctan(dy/dx))
        if(i == 0):
            m = np.zeros(len(dy))
        else:
            m = -b[i]*b[i]*(dx-h)/((dy-k[i])*(a*a))

        zl = zl + m.tolist()
    #
    # convert to numpy array
    #
    x = np.asarray(xl)
    y = np.asarray(yl)
    z = np.asarray(zl)


    #
    # steady as she goes
    #
    return x,y,z 


def vf(t,x,m):
    #
    # Vector field function
    #
    dx=np.zeros(2)
    zz = polyval2d(x[0], x[1], m)    
    theta = np.arctan(zz)
    dx[0]=np.cos(theta)
    dx[1]=np.sin(theta)

    #dx[1]=x[0]**2-x[0]-2
    #polyval2d(xx, yy, m)
    #dx[1]=polyval2d(xx, yy, m)
    return dx

def arr(m):
    #
    # Solution curves
    #
    h = hprime
    ic=[[h,-4],[h,-1],[h,1],[h,-8]]
    end = [2,2,2,2]
    t0=0; dt=0.1;
    r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
    for k in range(len(ic)):
        tEnd=np.sqrt(ic[k][0]**2 + ic[k][1]**2)-end[k]
        Y=[];T=[];S=[];
        r.set_initial_value(ic[k], t0).set_f_params(m)
        while r.successful() and r.t +dt < tEnd:
            r.integrate(r.t+dt)
            Y.append(r.y)

        S=np.array(np.real(Y))
        plt.plot(S[:,0],S[:,1], color = 'red', lw = 4.25)
    plt.hlines(Rprime, hprime, 0, color='red',lw = 4.25)


def polyfit2d(x, y, z, order=5):
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    for k, (i,j) in enumerate(ij):
        G[:,k] = x**i * y**j

    #
    cnd=1e-5
    #m, _, _, _ = np.linalg.lstsq(G, z,rcond=cnd)
    m, _, _, _ = np.linalg.lstsq(G, z)
    return m

def polyval2d(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        tmp = a * x**i * y**j
        z += tmp
        #print a,i,j,tmp,z
    return z

def polyval2d_disp(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        tmp = a * x**i * y**j
        z += tmp
        print a,i,j,tmp,z
    return z

#
#
#
def poly_disp_fparse(m):
    print "#"
    print "# Polynomial Interpolation Function"
    print "#"
    

    print "slope_func = '"

    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    for a, (i,j) in zip(m, ij):
        if( (i+1)*(j+1) != len(m)):
            print '               %.15f * x^%i * y^%i +' % (a,i,j )
        else:
            print "               %.15f * x^%i * y^%i'" % (a,i,j )

    print 
    return 0

#
#
#
def poly_disp_py(m):
    print "#"
    print "# Polynomial Interpolation Function"
    print "# For python"
    

    print "return ",
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    for a, (i,j) in zip(m, ij):
        if( (i+1)*(j+1) != len(m)):
            print '%.15f * x**%i * y**%i +' % (a,i,j ),
        else:
            print "%.15f * x**%i * y**%i" % (a,i,j ),

    print 
    return 0

#
#
#
def poly_disp_py_line(m):
    print "#"
    print "# Polynomial Interpolation Function"
    print "# For python"
    

    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    for a, (i,j) in zip(m, ij):
        if( (i+1)*(j+1) != len(m)):
            print '    tmp += %.15f * x**%i * y**%i' % (a,i,j )
            print '    print tmp'
        else:
            print "    tmp += %.15f * x**%i * y**%i" % (a,i,j )
            print '    print tmp'
    print 
    return 0

def load_ex():
    #
    # Generate Example Data
    #
    numdata = 100
    x = np.random.random(numdata)
    y = np.random.random(numdata)

    #
    # silly fake function for z
    #
    z = x**2 + y**2 + 3*x**3 + y + np.random.random(numdata)

    return x,y,z

#
# main function: execute
#
def main():

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # ----------------------------------------
    #
    # load data in
    #
    x,y,z=load_ell()
    #x,y,z=load_ex()

    #
    # Fit polynomial
    #
    m = polyfit2d(x,y,z)

    #
    # Evaluate it on a grid...
    #
    nx, ny = 200, 200
    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), nx), 
                         np.linspace(y.min(), y.max(), ny))
    zz = polyval2d(xx, yy, m)

    #
    # m is a matrix of polynomial values...
    # e.g. 

    #
    # Plot!
    #
    arr(m)
    # 
    # ----------------------------------------

    xt,yt,zt = top.load_ell()
    mt = polyfit2d(xt,yt,zt)
    nxt, nyt = 200, 200
    xxt, yyt = np.meshgrid(np.linspace(x.min(), x.max(), nx), 
                         np.linspace(y.min(), y.max(), ny))
    zzt = top.polyval2d(xxt, yyt, mt)
    top.arr(mt)

    #
    # ----------------------------------------
    
    plt.suptitle("SoV Configuration: Top Tier")
    plt.title("Eight Vane")

    xmin = -15
    xmax = 5

    ymin = -10
    ymax = 14

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
    R = Rprime
    circle=plt.Circle((0,0),R,color='black',linestyle='dotted',fill=False,linewidth=4)

    from matplotlib.patches import Ellipse, Arc
    ellipse = Arc([0.0,0.0],2*Rprime,2*Rprime,0,180,0,color='black', linewidth='5.0')
    ax.add_patch(ellipse)

    fig = plt.gcf()
    fig.gca().add_artist(circle)
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('interp_entire_top.png')
    plt.savefig('interp_entire_top.pdf', format='pdf', dpi=1000)
    #
    # output polynomial for input
    #
    poly_disp_fparse(m)    

#
# EXECUTE
#
main()


#
# nick 
# 4/28/16 
#
