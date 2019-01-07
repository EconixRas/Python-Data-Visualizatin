import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

multiplier = 1
x = [5, 10, 15, 20]
y = list(map(lambda x: x * multiplier, [4, 6, 8, 10]))

plt.subplots_adjust(left=0.1, bottom=0.2)
plt.axis([5, 25, 0, 100])

p, = plt.plot(x, y)

axSlider = plt.axes([0.1, 0.1, 0.8, 0.04], facecolor = 'r')
slider_y = Slider(axSlider, 'mlt', 1, 10, valinit=2, valstep=1)

def update_multiplier(mul_val):
	multiplier = mul_val
	p.set_ydata(list(map(lambda x: x * multiplier, [4, 6, 8, 10])))

slider_y.on_changed(update_multiplier)

plt.show()
