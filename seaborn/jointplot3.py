import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = sns.load_dataset('tips')

sns.set(style='darkgrid')
g = sns.jointplot('total_bill', 'tip', 
					kind='reg',
					xlim=(0, 60),
					ylim=(0, 12), 
					color='m',
					height=7,
					data=dataset)
plt.show()
