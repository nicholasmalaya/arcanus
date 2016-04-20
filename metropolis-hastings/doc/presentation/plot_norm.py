import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mean = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-3,3,100)
plt.plot(x,mlab.normpdf(x,mean,sigma))

# first point (reject)
x1=[-2.2]
y1=[0.25]
plt.plot(x1,y1,color='r', ms=10, marker='o')

# second point, accept
x2=[0.2]
y2=[0.15]
plt.plot(x2,y2,color='g', ms=10, marker='o')

# plot circle
fig = plt.gcf()
circle=plt.Circle((x2[0],y2[0]),.1,color='b')
fig.gca().add_artist(circle)


#ax = plt.gca()
#ax.set_xlim((-3,3))
#ax.set_ylim((0,1))
#plt.show()
plt.savefig('norm-corr.pdf')
