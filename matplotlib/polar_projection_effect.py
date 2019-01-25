#-----------------------------------------------------------------
# Polar Project Example
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(figsize=(7, 7))
"""
projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional

    The projection type of the Axes. str is the name of a costum projection, see projections. The default None results in a 'rectilinear' projection.
"""

n = 20
theta = np.arange(0, 2*np.pi, 2 * np.pi/n)
radius = 10*np.random.rand(n)
width = np.pi/4*np.random.rand(n)

ax = plt.axes([0.025, 0.025, 0.95, 0.95], projection='polar')
bars = plt.bar(theta, radius, width=width, bottom=0)

for r, b in zip(radius, bars):
	b.set_facecolor(plt.cm.jet(r/10))
	b.set_alpha(0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
