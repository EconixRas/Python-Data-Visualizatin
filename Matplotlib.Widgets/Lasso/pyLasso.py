import matplotlib.pyplot as plt
from matplotlib.widgets import Lasso

x = range(0, 100)
y = range(0, 100)

fig, ax = plt.subplots()
ax.plot(x, y)

def printCoordinate(x):
	print(x)

lso = Lasso(ax, (10, 10), printCoordinate)

plt.show()
