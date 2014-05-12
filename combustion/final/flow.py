#!/bin/py
#
#
#
import sys
import numpy as np
import pylab

def zprime(z):
    """Returns \bar z'z'"""
    return 1

#
# main function 
#
if __name__ == "__main__":

    # define field
    nx = 50
    ny = 31
    
    # sanity check
    if(ny%2 != 1):
        print 'ny must be odd!'
        print ny
        print sys.exit(1)

    # initialize 
    z = np.zeros(ny)
    
    #
    # enforce b.c. ( x < 0, y = 0 => z=1)
    #
    z[0:ny/2] = 1.0

    # spacing
    dx = 1 # centimeters
    dy = 1 # centimeters

    # Diffusivities
    DL = 0.176 # (cm^2/sec)
    DT = 10*DL

    u = 100 # 100 centimeters = 1 m/s
    
    #
    # spatial iteration loop!
    #
    zf = []
    zf.append(z)
    for i in xrange(nx):

        zt = np.zeros(ny)
        zt[0] = 1.0
        for j in xrange(1,ny-1):
            zt[j] = DT*dx*(z[j+1]-2*z[j]+z[j-1])/(u*dy*dy) + z[j]

        #
        # update mean field  and save state
        #
        z = zt
        zf.append(z)    
        #print (i+1)*dx, 'cm ',z

    #
    # plot solution of mean field 
    #
    y = np.arange(-dy*ny/2., dy*ny/2., dy)
    ind=0
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zf[ind], linewidth=2.0, label=t)
    pylab.xlabel('y (cm)',size=22.0)
    pylab.ylabel(r'$\bar z$', size=30.0)
    pylab.title(r'Mean value of the mixture fraction, $\bar z$')
    pylab.grid(True)

    #
    # 5 cm, 30 cm and 50 cm
    #
    ind=5
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zf[ind], linewidth=2.0, label=t)

    ind=30
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zf[ind], linewidth=2.0, label=t)

    ind=50
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zf[ind], linewidth=2.0, label=t)


    #
    # plot
    #
    pylab.show()

#
# nick 
# 5/9/14
#
