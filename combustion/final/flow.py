#!/bin/py
#
#
#
import sys
import numpy as np

def zprime(z):
    """Returns \bar z'z'"""
    return 1

#
# main function 
#
if __name__ == "__main__":

    # define field
    nx = 5
    ny = 11
    
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
    dx = 5 # centimeters
    dy = 5 # centimeters

    # Diffusivities
    DL = 0.176 # (cm^2/sec)
    DT = 10*DL

    u = 100 # 100 centimeters = 1 m/s
    
    #
    # spatial iteration loop!
    #
    print z
    for i in xrange(nx):

        zt = np.zeros(ny)
        zt[0] = 1.0
        for j in xrange(1,ny-1):
            zt[j] = DT*dx*(z[j+1]-2*z[j]+z[j-1])/(u*dy*dy) + z[j]
        # update mean field 
        z = zt
        
        print z


#
# nick 
# 5/9/14
#
