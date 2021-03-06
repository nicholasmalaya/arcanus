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

hprime = -4.5

def load_ell():
    #
    # Generate Data from ellipses
    #
    h           = hprime
    thetaf      = 20*np.pi/180.
    a           = -h*1.0
    miny        = -0.0

    #
    # create data
    # 
    space   = 0.02
    R       = 3.0
    y0      = np.arange(1.5,miny,-space)
    #print y0
    #y0 = np.array([1.5, 1.45, 1.35, 1.2, 1.05, 0.9, 0.6, 0.3, 0.15])


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
    ic=[[h,-2],[h,0.8],[h,-1],[h,-3],[h,1.5],[h,0],[h,-3.3]]
    t0=0; dt=0.1;
    r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
    for k in range(len(ic)):
        tEnd=np.sqrt(ic[k][0]**2 + ic[k][1]**2)-0.5
        Y=[];T=[];S=[];
        r.set_initial_value(ic[k], t0).set_f_params(m)
        while r.successful() and r.t +dt < tEnd:
            r.integrate(r.t+dt)
            Y.append(r.y)

        S=np.array(np.real(Y))
        plt.plot(S[:,0],S[:,1], color = 'red', lw = 4.25)

def polyfit2d(x, y, z, order=5):
    ncols = (order + 1)**2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order+1), range(order+1))
    for k, (i,j) in enumerate(ij):
        G[:,k] = x**i * y**j

    #
    # http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.lstsq.html
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
    # extent: [ None | (x0,x1,y0,y1) ]
    #
    plt.imshow(zz, extent=(x.min(), x.max(), y.min(), y.max()))
    plt.colorbar()
    plt.scatter(x, y, c=z)

    plt.title("Elliptic Vane Interpolation")
    plt.xlim([-7,1])
    plt.ylim([-5,2])
    plt.xlabel('Streamwise (x)')
    plt.ylabel('Spanwise (y)')

    # add circle
    R = 1.5
    circle=plt.Circle((0,0),R,color='black',fill=False,linewidth=4)
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    plt.savefig('interp_front.png')

    #
    # output polynomial for input
    #
    poly_disp_fparse(m)    

    #poly_disp_py_line(m)
    #print
    #print polyval2d_disp(-5.5, -3.5, m)
#
# EXECUTE
#
main()


#
# nick 
# 1/30/16 
#
# http://stackoverflow.com/questions/7997152/python-3d-polynomial-surface-fit-order-dependent
#
