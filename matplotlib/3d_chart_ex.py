#-----------------------------------------------------------------
# 3D Chart Example
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(x, y)
radius = np.sqrt(x**2 + y**2)
z = np.sin(radius)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(x, y, z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2, 1)

plt.show()
