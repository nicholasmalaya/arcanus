from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y = np.mgrid[-np.pi/2.:np.pi/2:0.1, -10*np.pi/2:10*np.pi/2.:0.1]
Z = - np.cos(X) * np.cos(Y/10)

surf = ax.plot_surface(X, Y, Z, cmap='autumn', cstride=4, rstride=4)
ax.set_title("-cos(x)cos(y/10)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x,y)")

plt.savefig("3d.pdf")
plt.show()
