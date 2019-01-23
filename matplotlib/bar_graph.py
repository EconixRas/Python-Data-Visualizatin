#-----------------------------------------------------------------
# simple bar graph
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.arange(n)
y1 = np.random.randint(0, 100, n)
y2 = np.random.randint(0, 100, n)

print(x)
print(y1)
print(-y2)

fig, ax = plt.subplots()
ax.bar(x, y1, color='yellow', edgecolor='black')
ax.bar(x, -y2, color='green', edgecolor='black')

for a,b in zip(x,y1):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom')

for a,b in zip(x,y2):
    plt.text(a, -b-10, '%.0f' % b, ha='center', va='bottom')

ax.axis([-1, 10, -110, 110])

plt.show()
