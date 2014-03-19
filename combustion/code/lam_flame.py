#!/bin/py
#
# simulate a convection-diffusion equation 
#
# mesh is equally spaced
#
import numpy as np
from pylab import *
import sys

# timestep 
dt = .01

# number of points
n = 100

# radii
r0   = 10.0
rinf = 20.0
dr = (rinf-r0)/n

#
r = np.arange(r0,rinf,dr)

# number of timesteps
steps = 1000

save = 100

# Diffusion Coefficient
D = 0.1
#D = 0.97*10**-5

print 'Running with:'
print 'dr ', dr
print 'n  ', n
print 'dt ', dt
print 'r_i ', rinf
print 'r_0 ', r0
print 'steps ',steps
print r

beta     = np.zeros(n)
beta_new = np.zeros(n)


T        = np.ones(n)
Yf       = np.zeros(n)
Yo       = np.ones(n)

Ti = 273

#
# set initial conditions on beta
# 
beta[0]=1.0
beta[-1]=0.0

beta_new[0]=1.0
beta_new[-1]=0.0

#
# initial conditions on Yf,Y0
#
Yf[0]=1.0
Yo[0]=0.0

if(dr*dr / (2*D) > dt):
    print 'warning: CFL condition exceeded!'
    #sys.exit(1)

nf = 1
no = 5
wo = 15.99
wf = 44.1

frac = wo*no/(wf*nf)

# heat release
q= 2220.0

# specific heat capacity
cp = 1.009
qcp = q/cp

#
# temporal loop
#
for t in xrange(steps):
    
    # space loop (ignores BCs)
    for i in xrange(1,n-1):
        rhalf  = (r[i+1]+r[i])/2.
        rmhalf = (r[i]+r[i-1])/2.        

        #
        # advance using finite difference
        #
        beta_new[i] = beta[i] + dt * D * (rhalf*rhalf * (beta[i+1]-beta[i])/dr - rmhalf*rmhalf * (beta[i]-beta[i-1])/dr)/(r[i]*r[i] * dr)

    # save plot of conserved scalar at special times
    #if( t%save == 0):
    #    plot(r,beta_new,label=t)

    #
    # save new timestep
    #
    beta = beta_new

    # ------------------------------------------------------------
    # now calculate surrogate quantities (on fuel side)
    # ------------------------------------------------------------
    # (flame front)
    #sf = Yo[-1] / (Yo[-1] + frac*Yf[0])
    #print 'steady state flame front at: ',sf
    
    #
    # (temperature)
    #
    T = Ti * beta + (Ti + qcp*Yo[-1]/frac)*(1-beta)

    # save plot of temperature at special times
    #if( t%save == 0):
    #    plot(r,T,label=t)

    # 
    # (Yf)
    #
    Yf = Yf[0]*beta + (beta-1)*Yo[-1]/frac

    # save plot of temperature at special times
    #if( t%save == 0):
    #    plot(r,Yf,label=t)

    Yn = (1-beta)
    #if( t%save == 0):
    #    plot(r,Yn,label=t)

    # ------------------------------------------------------------
    # calculate on oxidizer side
    # ------------------------------------------------------------
    
    T = (Ti * (1-beta) + (Yf[0]*qcp + Ti)*beta)
    #Yo = (Yo[-1]*(1-beta) - beta*Yf[0]/frac)
    Yo = Yo[-1]*(1-beta)

    # save plot of temperature at special times
    if( t%save == 0):
        #plot(r,Yf,label=t)
        plot(r,-Yf/.55,label=t)
        


#
# plot
# 
ylim([0,1])
show()


#
# nick 
# 3/15/14
#
