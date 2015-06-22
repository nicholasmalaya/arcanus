

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0,3.0,5.0])
y = np.array([0.144,1.826,6.842])

plt.loglog(x, y, '-o', basex=10)

plt.legend(loc='best')
#
# plot
#
plt.ylabel("Kinetic Energy Flux (Watts)")
plt.xlabel("Apparatus Diameter (Meters)")

#plt.show()
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('ke_exponent.png')


#
# nick
# 6/21/15
#
