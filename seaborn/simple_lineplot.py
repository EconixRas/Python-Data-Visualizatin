#######################################################
# Simple lineplot
#######################################################
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white')
dataset = sns.load_dataset('fmri')

print(dataset)
sns.lineplot(x='timepoint', y='signal', hue='region', 
			 style='event', data=dataset)

plt.show()
