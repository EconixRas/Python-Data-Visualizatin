#-----------------------------------------------------------------
# sample linear regression 2 x 2
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# make graph title a little bit more bold
sns.set(style='ticks')

# load sample anscombe dataset
data_set = sns.load_dataset('anscombe')

# plot the linear regression 
sns.lmplot(	x='x', y='y', col='dataset', 
			data=data_set, hue='dataset',
			col_wrap=2, palette='muted',
			height=3,
			scatter_kws={'s': 30, 'alpha': 0.8})

plt.show()
