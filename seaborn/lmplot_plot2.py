import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('iris')
sns.set()
g = sns.lmplot(x='sepal_length', y='sepal_width', hue='species',
				truncate=True,
				height=5,
				data=dataset)
g.set_axis_labels('Sepal length (mm)', 'Sepcal width (mm)')
plt.show()
