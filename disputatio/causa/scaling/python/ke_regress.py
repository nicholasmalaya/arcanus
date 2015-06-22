

import numpy as np
import matplotlib.pyplot as plt

sx = np.array([38.0])
sy = np.array([2491])

#x = np.array([0.0,1.0,3.0,5.0])
#y = np.array([0.0,0.144,1.826,6.842])

x = np.array([1.0,3.0,5.0])
y = np.array([0.144,1.826,6.842])

#x = np.array([1.0,3.0,5.0])
#y = 60*np.array([0.144,1.826,6.842])

plt.plot(x,y,'o',color='black',label='Simulation Data')
plt.plot(sx,sy,'o',color='green',label='Sinclair Data')

#
# fit with np.polyfit
#
m, b             = np.polyfit(x, y, 1)
alpha,beta,gamma = np.polyfit(x, y, 2)
a,s,d,f = np.polyfit(x, y, 3)
q,w,e,r,t = np.polyfit(x, y, 4)

xp = np.linspace(0.0, 40.0, num=20)
plt.plot(xp, m*xp + b, '-',label=r'D Scaling')
plt.plot(xp, alpha*xp*xp + beta*xp + gamma, '-',label=r'$D^2$ Scaling')
plt.plot(xp, a*xp**3 + s*xp**2 + d*xp + f, '-',label=r'$D^3$ Scaling')
plt.plot(xp, q*xp**4 + w*xp**3 + e*xp**2 + r*xp + t, '-',label=r'$D^4$ Scaling')


#plt.axvline(x=38,color='red')
plt.legend(loc='best')
plt.xlim(0.0,40)
plt.ylim(0.0,6000)
#
# plot
#
plt.ylabel("Kinetic Energy Flux (Watts)")
plt.xlabel("Apparatus Diameter (Meters)")

#plt.show()
plt.savefig('ke_regression.png')


#
# nick
# 6/21/15
#
