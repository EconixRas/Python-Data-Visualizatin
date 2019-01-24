#-----------------------------------------------------------------
# Plot sin, cos
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

n = 256

# Return evenly spaced numbers over a specified interval
x = np.linspace(-np.pi, np.pi, n)

# cos and sin variables
cos = np.cos(x)
sin = np.sin(x)

# plotting
plt.figure(figsize=(7,5))
plt.subplot(1, 1, 1)
plt.plot(x, cos, color='tomato', linewidth=2, linestyle='-')
plt.plot(x, sin, color='teal', linewidth=2, linestyle='-')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

plt.show()
