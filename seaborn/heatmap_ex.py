#-----------------------------------------------------------------
# seaborn heatmaps
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

sns.set() # remove label hyphen

dataset = sns.load_dataset('flights')
flights = dataset.pivot('month', 'year', 'passengers')
print(flights)
fig, ax = plt.subplots(figsize=(7,7))
sns.heatmap(flights, annot=True, fmt='d', linewidths=5, ax=ax)
plt.show()
