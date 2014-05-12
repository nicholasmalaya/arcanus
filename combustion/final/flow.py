#!/bin/py
#
#
#
import sys
import numpy as np
import pylab
import scipy.special as ss

def beta(a, b, mew):
    e1 = ss.gamma(a + b)
    e2 = ss.gamma(a)
    e3 = ss.gamma(b)
    e4 = mew ** (a - 1)
    e5 = (1 - mew) ** (b - 1)
    return (e1/(e2*e3)) * e4 * e5
 
def plot_beta(a, b):
    Ly = []
    Lx = []
    mews = np.mgrid[0:1:1000j]
    for mew in mews:
        Lx.append(mew)
        Ly.append(beta(a, b, mew))
    pylab.plot(Lx, Ly, linewidth=3.0)

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
    pylab.title(r'Mean value of the mixture fraction, $\bar z$ at several x-locations. ')
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
    pylab.close()
    
    # --------------------------------------------------
    #
    # calculate and plot PDF of mixture fraction!
    #
    # --------------------------------------------------

    #
    # y = 0, x = 30 (should look gaussian)
    #
    ind = 30 
    yloc = ny/2.
    zbar  = zf[ind][yloc]
    zzbar = zzf[ind][yloc]
    gamm = (zbar * (1 - zbar ) / (zzbar*zzbar) ) - 1
    if(gamm < 0):
        gamm = 0
    alph = zbar * gamm
    bet  = (1-zbar)*gamm
    plot_beta(alph, bet)

    #
    # plot at y = 15, x = 30 (should look like a delta function)
    # 
    ind = 30 
    yloc = ny-1
    zbar  = zf[ind][yloc]
    print zbar
    zzbar = zzf[ind][yloc]
    #gamm = (zbar * (1 - zbar ) / (zzbar*zzbar) ) - 1
    gamm = 10000
    alph = zbar * gamm
    bet  = (1-zbar)*gamm
    plot_beta(.01, 1)

    #
    # generic plot options
    #
    pylab.xlabel(r'$\bar z$',size=22.0)
    pylab.ylabel(r'$P(\bar z)$', size=30.0)

    pylab.xlim(0.0, 1.0)
    pylab.ylim(0.0, 6.0)
    pylab.legend()
    pylab.savefig('pdf.pdf')


#
# nick 
# 5/9/14
#
