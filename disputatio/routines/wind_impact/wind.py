#!/bin/py

# m/s   |  hot   | cold 
# 3        34.9  | 29.8
# 2        40.09 | 9.3
# 1        34.5  | .8745
# 0        20.0  | 0.0
#

speed = [0,1,2,3]
hot   = [20.0,34.5,40.09,34.9]
cold  = [0.0,.8745,9.3,29.8]


#
#
#
import matplotlib.pyplot as plt

plt.plot(speed,hot,'o', label='Hot')
plt.plot(speed,cold,'o', label='Cold')

#overrx = np.linspace(1.0, 5.0, num=50)
plt.xlim([0,5])
plt.ylim([0,45])

fsz=20
plt.ylabel(r'Kinetic Energy Flux (Watts)',
           fontsize=fsz,labelpad=20)

plt.xlabel(r'Wind Speed (m/s)',fontsize=fsz)


# might not need this
#plt.axes().set_aspect('equal', 'datalim')

plt.legend(loc='best')
plt.tight_layout()
#plt.show()
plt.savefig('wind_impact.png')


#
# nick 
# 10/14/16
#
