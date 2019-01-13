import matplotlib.pyplot as plt
from matplotlib.widgets import Button

x = list(range(0, 11))
y = list(range(0, 110, 10))

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
p, = plt.plot(x, y, linewidth=2, color='blue')

ICON_Python = plt.imread('python-icon.png')

axButton1 = plt.axes([0.1, 0.1, 0.1, 0.1]) #left, bottom, width, height
btn1 = Button(	ax=axButton1,
				label='Green',
				# image=ICON_Python,
				color='teal',
				hovercolor='tomato')

def color_green(event):
	p.set_color('green')
	plt.draw()
btn1.on_clicked(color_green)

axButton2 = plt.axes([0.3, 0.1, 0.1, 0.1])
btn2 = Button(axButton2, 'Red')

def color_red(event):
	p.set_color('red')
	plt.draw()
cid = btn2.on_clicked(color_red)
btn2.disconnect(cid)

plt.show()
