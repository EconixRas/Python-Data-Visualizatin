import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('iris')
iris = pd.melt(dataset, 'species', var_name='measurement')

sns.set(style='whitegrid')
fig, ax = plt.subplots()
sns.despine(bottom=True, left=True)
sns.stripplot(	x='value',
				y='measurement',
				hue='species',
				dodge=True,
				jitter=True,
				alpha=0.25,
				zorder=1,
				data=iris)

sns.pointplot(	x='value',
				y='measurement',
				hue='species',
				dodge=.532,
				join=False,
				palette='dark',
				markers='d',
				scale=.75,
				ci=None,
				data=iris)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[3:], labels[3:], title='species',
			handletextpad=0,
			columnspacing=1,
			loc='lower right',
			ncol=3,
			frameon=True)
plt.show()

