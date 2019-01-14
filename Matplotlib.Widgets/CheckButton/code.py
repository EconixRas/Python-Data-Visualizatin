import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

x = range(0, 11)
y1 = [10] * 11
y2 = [20] * 11
y3 = [30] * 11

fig, ax = plt.subplots()
p1, = ax.plot(x, y1, color='red', label='red')
p2, = ax.plot(x, y2, color='blue', label='blue', visible=False)
p3, = ax.plot(x, y3, color='green', label='green', visible=False)
lines = [p1, p2, p3]

plt.axis([-2.5, 12, 0, 40])
plt.subplots_adjust(left=0.25, bottom=0.1, right=0.95, top=0.95)

labels = ['red', 'blue', 'green']
actives = [True, False, False] # set the checkbox as checked on displaying
axCheckButton = plt.axes([0.03, 0.4, 0.15, 0.15]) # left, bottom, width, height
chxbox = CheckButtons(axCheckButton, labels, actives)

def set_visible(label):
	index = labels.index(label)
	lines[index].set_visible(not lines[index].get_visible())
	plt.draw()

cid = chxbox.on_clicked(set_visible)
# chxbox.disconnect(cid)

print(chxbox.get_status())

# chxbox.set_active(1)

plt.show()
