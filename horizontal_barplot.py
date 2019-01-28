import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('car_crashes').sort_values('total', ascending=False)

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(6, 11))
# plot the total data
sns.set_color_codes('pastel')
sns.barplot(x='total', y='abbrev',
			label='Total',
			color='b',
			data=dataset)

# plot the subset on top of the total
sns.set_color_codes('muted')
sns.barplot(x='alcohol', y='abbrev',
			label='Alcohol-involved',
			color='b',
			data=dataset)

# labels
ax.legend(ncol=2, loc='lower right')
ax.set(xlim=(0, 25), xlabel='Auto collisions per billion miles', 
		ylabel='')
sns.despine(bottom=True,left=True)
plt.show()
