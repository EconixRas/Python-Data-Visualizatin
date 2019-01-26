#-----------------------------------------------------------------
# Simple Pie Chart example
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

n = 20
data_series = np.ones(n)
data_series[-1] *= 2

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.pie(data_series, 
		explode=data_series*0.05, 
		colors=[(0.55, i/n, 0.5) for i in range(1, n+1)])
plt.show()
