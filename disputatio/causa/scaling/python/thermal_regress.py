

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0,3.0,5.0])
y = np.array([0.089,0.18,0.31])

plt.plot(x,y,'o',color='black',label='Data')

#
# fit with np.polyfit
#
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, '-',label='Linear Regression')
plt.legend(loc='best')
plt.xlim(0,6)
#
# plot
#
plt.ylabel("Thermal Diameter")
plt.xlabel("Apparatus Diameter")

#plt.show()
plt.savefig('scaling_regression.png')


#
# nick
# 6/21/15
#
