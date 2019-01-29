import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('exercise')

sns.set(style='darkgrid')
g = sns.catplot( x='time',
				 y='pulse',
				 hue='kind',
				 col='diet',
				 capsize=.2,
				 palette='YlGnBu_d',
				 height=6,
				 aspect=.75,
				 kind='point',
				 data=dataset)
g.despine(left=True)
plt.show()
