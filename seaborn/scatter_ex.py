#######################################################
# scatterplot graph examples (Diamond Price vs Carat)
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
data_set = sns.load_dataset('diamonds')
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

fig, ax = plt.subplots(figsize=(6.5, 6.5))
sns.scatterplot(x='carat', y='price',
				hue='clarity', size='depth',
				palette="ch:r=-.2,d=.3_r",
				hue_order=clarity_ranking,
				sizes=(1, 8), 
				linewidth=0,
				data=data_set, ax=ax)

sns.despine(fig, left=True, bottom=True)
plt.show()
