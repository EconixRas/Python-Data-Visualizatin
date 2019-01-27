#######################################################
# cubehelix palettes examples
#######################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')
rs = np.random.RandomState(50)

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(7, 7), 
							sharex=True,
							sharey=True)

for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):
	cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)

	x, y = rs.randn(2, 50)
	sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)
	ax.set(xlim=(-3, 3), ylim=(-3, 3))

fig.tight_layout()
plt.show()
