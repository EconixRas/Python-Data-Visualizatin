#######################################################
# Grouped boxplots
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style='ticks', palette='pastel')
dataset = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill',
			hue='smoker', palette=['m', 'g'],
			data=dataset)
sns.despine(offset=10, trim=True)
print(dataset)
plt.show()
