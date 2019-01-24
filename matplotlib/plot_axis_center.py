#-----------------------------------------------------------------
# Plot with x-axis and y-axis in the center
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,5))
ax = plt.subplot(1, 1, 1)

# remove top and bottom borders
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# reposition left and bottom borders
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

n = 256
x = np.linspace(-np.pi, np.pi)
cos, sin = np.cos(x), np.sin(x)

plt.plot(x, cos, color='tomato', linewidth=2, linestyle='-', label='cos')
plt.plot(x, sin, color='teal', linewidth=2, linestyle='-', label='sin')

plt.xticks(	[-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
			[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks(	[-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# Optional. If you want to hide center tick labels
# plt.xticks(	[-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
# 			[r'$-\pi$', r'$-\pi/2$', '', r'$+\pi/2$', r'$+\pi$'])
# plt.yticks(	[-1, 0, +1], [r'$-1$', '', r'$+1$'])

plt.legend(loc='upper left', frameon=False)
plt.show()
