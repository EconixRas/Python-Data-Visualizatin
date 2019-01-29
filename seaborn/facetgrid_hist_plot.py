#######################################################
# Facetting histograms by subsets of data
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset = sns.load_dataset('tips')
sns.set(style='darkgrid')
bins = np.linspace(0, 60, 13)
g = sns.FacetGrid(dataset, row='sex', col='time', margin_titles=True)
g.map(plt.hist, 'total_bill', color='steelblue', bins=bins)
plt.show()
