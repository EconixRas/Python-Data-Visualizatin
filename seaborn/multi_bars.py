#######################################################
# Plot multiple bar graphs using seaborn
#######################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# options: white, dark, whitegrid, darkgrid, ticks
sns.set(style='white', context='talk')
rs = np.random.RandomState(8)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 6), sharex=True)
x = np.array(list('ABCDEFGHIJ'))

# Graph #1
y1= np.arange(1, 11)
sns.barplot(x=x, y=y1, palette='rocket_r', ax=ax1)
ax1.axhline(0, color='k', clip_on=False)
ax1.set_ylabel('y1')

# Graph #2
y2 = y1 - 5.5
sns.barplot(x=x, y=y2, palette='CMRmap', ax=ax2)
ax2.axhline(0, color='k', clip_on=False)
ax2.set_ylabel('y2')

# Graph 3
y3 = rs.choice(y1, len(y1))
sns.barplot(x=x, y=y3, palette='CMRmap_r', ax=ax3)
ax3.axhline(0, color='k', clip_on=False)
ax3.set_ylabel('y3')

sns.despine(bottom=True)
plt.setp(fig.axes, yticks=[])
plt.tight_layout(h_pad=2)
plt.show()
