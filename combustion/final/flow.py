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
    """ run a simulation, and plot everything up"""
    #
    # define field
    #
    nx = 50
    ny = 91
    
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
    z[0:ny/2 +1] = 1.0

    # spacing
    dx = 1 # centimeters
    dy = 0.2 # centimeters

    # Diffusivities
    DL = 0.176 # (cm^2/sec)
    DT = 10*DL

    u = 100 # 100 centimeters = 1 m/s
    
    # --------------------------------------------------
    #
    # spatial iteration loop!
    #
    # --------------------------------------------------
    zf = []
    zf.append(z)

    zzf = []
    zzf.append(np.zeros(ny))

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

        #
        # calculate fluctuation \bar (z'z')
        #
        zzt = np.zeros(ny)
        for j in xrange(1,ny-1):
            #zzt[j] = 0.5*((z[j+1]-z[j])/dy)**2 * DT * (i*dx)/u
            zzt[j] = 0.25*((z[j+1]-z[j-1])/dy)**2 * DT * (i*dx)/u
        
        zzf.append(zzt)

    # --------------------------------------------------   
    #
    # plot solution of mean field 
    #
    # --------------------------------------------------
        
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
    # plot mean field
    #
    pylab.xlim([-5,5])
    pylab.ylim([-0.1,1.1])
    pylab.legend()
    pylab.savefig('mean.pdf')
    pylab.close()

    # --------------------------------------------------
    #
    # calculate and plot fluctuation!
    #
    # --------------------------------------------------

    ind=0
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zzf[ind], linewidth=2.0, label=t)
    pylab.xlabel('y (cm)',size=22.0)
    pylab.ylabel(r'$\bar{z^{\prime}z^{\prime}}$', size=30.0)
    pylab.title(r'Fluctuating value of the mixture fraction')
    pylab.grid(True)

    ind=4
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zzf[ind], linewidth=2.0, label=t)

    ind=30
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zzf[ind], linewidth=2.0, label=t)

    ind=50
    t='x = '+str(ind*dx)+' cm'
    pylab.plot(y,zzf[ind], linewidth=2.0, label=t)

    #
    # plot fluctuation
    #
    pylab.legend()
    pylab.savefig('fluc.pdf')
    pylab.show()
    
    

#
# nick 
# 5/9/14
#
