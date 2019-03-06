import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

raw_data = pd.read_csv('scores.csv')
data = raw_data[:5][['School Name', 'Average Score (SAT Math)', 'Average Score (SAT Reading)',
       'Average Score (SAT Writing)']]
schools = data.iloc[:, 0]
barMath = data.iloc[:, 1]
barReading = data.iloc[:, 2]
barWriting = data.iloc[:, 3]
indx = np.arange(len(data))

plt.figure(figsize=(10,7))
barWidth = 0.35
graphMath = plt.bar(x=indx, height=barMath, width=barWidth)
graphReading = plt.bar(x=indx, height=barReading, width=barWidth, bottom=barMath)
graphWriting = plt.bar(x=indx, height=barWriting, width=barWidth, bottom=barReading+barMath)

plt.xlabel('Schools')
plt.ylabel('SAT Scores')

schools = ['\n'.join(wrap(school, 15)) for school in schools]
plt.xticks(indx, schools)
plt.yticks(np.arange(0, 2400, 2400/len(indx)))
plt.title('Average SAT Scores for NYC Public School')
plt.show()
