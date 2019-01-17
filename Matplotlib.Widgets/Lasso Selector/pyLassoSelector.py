import matplotlib.pyplot as plt
from matplotlib.widgets import LassoSelector

fig, ax = plt.subplots()

def onSelect(x):
	print(x)

def onPress(event):
	print('Pressed')

def onRelease(event):
	print('Released')

lineprops = {'color': 'red', 'linewidth': 4, 'alpha': 0.8}
lsso = LassoSelector( ax=ax, onselect=onSelect, lineprops=lineprops, button=1)

fig.canvas.mpl_connect('button_press_event', onPress)
fig.canvas.mpl_connect('button_release_event', onRelease)

plt.show()
