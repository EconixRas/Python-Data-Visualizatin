#######################################################
# FacetGrid  boxplots
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


r = np.linspace(0, 10, num=100)
df = pd.DataFrame({'r':r, 'slow':r, 'medium':2, 'fast':4*r})
df = pd.melt(df, id_vars=['r'], var_name='speed', value_name='theta')

sns.set()
g = sns.FacetGrid(	df, 
					col='speed',
					hue='speed',
					subplot_kws={'projection':'polar'},
					height=4.5,
					sharex=False,
					sharey=False,
					despine=False	)
g.map(sns.scatterplot, 'theta', 'r')
plt.show()
