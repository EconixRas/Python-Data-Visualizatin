#-----------------------------------------------------------------
# Gridline Formatting
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(1,1,1)
axes.axis([0, 4, 0, 3]) 

axes.xaxis.set_major_locator(MultipleLocator(1.0)) # set x-axis major unit with 1.0 interval
axes.xaxis.set_minor_locator(MultipleLocator(0.1)) # set x-axis minor unit with 0.1 interval
axes.yaxis.set_major_locator(MultipleLocator(1.0)) # set y-axis major unit with 1.0 interval
axes.yaxis.set_minor_locator(MultipleLocator(0.1)) # set y-axis minor unit with 0.1 interval

# draw major gridline
axes.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='lime', alpha=0.5)
axes.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='lime', alpha=0.5)

# draw minor gridline
axes.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='firebrick', alpha=0.5)
axes.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='firebrick', alpha=0.5)

# remove tick labels
axes.set_xticklabels([])
axes.set_yticklabels([])

plt.show()
