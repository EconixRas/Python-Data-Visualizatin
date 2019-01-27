#######################################################
# Grouped barplots
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
dataset = sns.load_dataset('titanic')
print(dataset)

graph = sns.catplot(x='class', y='survived', 
					hue='sex',
					height=6,
					kind='bar',
					palette='muted',
					data=dataset)
graph.set_ylabels('survival probability')

plt.show()
