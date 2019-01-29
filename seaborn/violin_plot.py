#######################################################
# Grouped violinplots with split violins
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('tips')

sns.set(style='whitegrid', palette='pastel', color_codes=True)
sns.violinplot(x='day', y='total_bill', 
				hue='smoker',
				split=True,
				inner='quart',
				palette={'Yes':'y', 'No':'b'},
				data=dataset)
sns.despine(left=True)
plt.show()
