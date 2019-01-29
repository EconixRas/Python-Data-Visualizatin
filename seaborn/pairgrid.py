import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('titanic')
sns.set(style='whitegrid')
g = sns.PairGrid(dataset, y_vars='survived',
					x_vars=['class', 'sex', 'who', 'alone'],
					height=5, 
					aspect=.5)

g.map(sns.pointplot, scale=1.3, errwidth=4, color='xkcd:plum')
g.set(ylim=(0, 1))
sns.despine(fig=g.fig, left=True)
plt.show()
