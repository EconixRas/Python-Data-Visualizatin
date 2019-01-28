import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='ticks')
n = 1000
rs = np.random.RandomState(10)

# Draw samples from a Gamma distribution.
# Samples are drawn from a Gamma distribution with specified parameters, shape 
# (sometimes designated “k”) and scale (sometimes designated “theta”), where both parameters are > 0.
x = rs.gamma(2, size=n)
y = -.5 * x + rs.normal(size=n)
sns.jointplot(x, y, kind='hex', color='b')
plt.show()
