import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

rs = np.random.RandomState(10)
mean = [0, 0]
cov = [(1, .5), (.5, 1)]
x1, x2 = rs.multivariate_normal(mean, cov, 500).T
x1 = pd.Series(x1, name='$X_1$')
x2 = pd.Series(x2, name='$X_2$')
g = sns.jointplot(x1, x2, kind='kde', height=7, space=0)
plt.show()
