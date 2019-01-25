#-----------------------------------------------------------------
# matplotlib animation example
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
import numpy as np

# Turn off toolbar
matplotlib.rcParams['toolbar'] = 'None'

# Generate data
n, size_min, size_max = 50, 50, 2500

# circles' position
pos = np.random.uniform(0, 1, (n, 2))

# circles' color
colors = np.ones((n, 4)) * (0, 0, 0, 1)

# transparent level
colors[:, 3] = np.linspace(0, 1, n)

# circle size
csize = np.linspace(size_min, size_max, n)

# plotting
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.005, 0.005, 0.990, 0.990], aspect=1)
scat_graph = ax.scatter(pos[:, 0], pos[:, 1], s=csize, linewidth=0.5, edgecolors=colors, facecolors='None')

# remove tick labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# animation effect function
def update(frame):
	global pos, colors, csize

	# transparency
	colors[:, 3] = np.maximum(0, colors[:, 3] - 1.0/n)

	# increase the size when apply animation
	csize += (size_max - size_min) / n

	# frame rate
	i = frame % 50
	pos[i] = np.random.uniform(0, 1, 2)
	csize[i] = size_min
	colors[i, 3] = 1

	# update scatter graph
	scat_graph.set_edgecolor(colors)
	scat_graph.set_sizes(csize)
	scat_graph.set_offsets(pos)
	return scat_graph

# creates animation effect (n frame per second)
animation = FuncAnimation(fig, update, interval=5)

plt.show()
