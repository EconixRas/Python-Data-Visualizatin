#######################################################
# Facetting histograms by subsets of data
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset = sns.load_dataset('dots')
print(dataset)

sns.set(style='ticks')

palette = dict(zip(dataset.coherence.unique(),
				sns.color_palette('rocket_r', 6)))
print(palette)
sns.relplot( x='time',
			 y='firing_rate',
			 hue='coherence',
			 size='choice',
			 col='align',
			 size_order=['T1', 'T2'],
			 palette=palette,
			 height=5,
			 aspect=0.75,
			 facet_kws=dict(sharex=False),
			 kind='line',
			 legend='full',
			 data=dataset)

plt.show()
