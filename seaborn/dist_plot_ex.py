#######################################################
# Distribution graph examples
#######################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', palette='Accent_r', color_codes=True)
rs = np.random.RandomState(1)

# set up matplotlib figure and axes
fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.despine(top=True, bottom=False, left=True, right=True)

data = rs.normal(size=100)
sns.distplot(data, kde=False, color='teal', ax=axes[0, 0])
sns.distplot(data, hist=False, rug=True, color='tomato', ax=axes[0, 1])
sns.distplot(data, hist=False, color='lightgreen', kde_kws={'shade': True}, ax=axes[1, 0])
sns.distplot(data, color='purple', ax=axes[1, 1])

plt.setp(axes, yticks=[])
plt.tight_layout()
plt.show()
