#!/bin/py

# m/s   |  hot   | cold 
# 3        34.9  | 29.8
# 2        40.09 | 9.3
# 1        34.5  | .8745
# 0        20.0  | 0.0
#

import numpy as np

speed = [0,1,2,3]
s     = [0]
#h     = [7.0,12.5,30.09,54.9]
h     = [7.0]
c     = [0.0,.8745,7.3,24.8]


hot  = 11.65*np.array(h)
cold = 11.65*np.array(c)

#
#
#
import matplotlib.pyplot as plt

fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)

plt.plot(s,hot,'v-', label='Hot Wind',linewidth=4,markersize=30,color='blue')
plt.plot(speed,cold,'o--', label='Cold Wind',linewidth=4,markersize=10,color='green')

#overrx = np.linspace(1.0, 5.0, num=50)
plt.xlim([-.3,3.5])
plt.ylim([0,700])

fsz=20
plt.ylabel(r'Kinetic Energy Flux (Watts)',
           fontsize=fsz)

plt.xlabel(r'Wind Speed (m/s)',fontsize=fsz)


# might not need this
#plt.axes().set_aspect('equal', 'datalim')

plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('wind_one.png')


#
# nick 
# 10/14/16
#
