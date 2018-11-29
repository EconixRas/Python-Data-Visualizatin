import numpy as np
import pandas as pd
from textwrap import wrap

raw_data = pd.read_csv('scores.csv')
data = raw_data[:5][['School Name', 'Average Score (SAT Math)', 'Average Score (SAT Reading)', 'Average Score (SAT Writing)']]
schools = data.iloc[:, 0]
barMath = data.iloc[:, 1]
barReading = data.iloc[:, 2]
barWriting = data.iloc[:, 3]
indx = np.arange(len(data))

# plot bar graph
column_width = 0.35

plt.figure(figsize=(10, 7))

graphMath = plt.bar(x=indx, height=barMath, width=column_width)
graphReading = plt.bar(x=indx, height=barReading, width=column_width, bottom=barMath)
graphWriting = plt.bar(x=indx, height=barWriting, width=column_width, bottom=barReading+barMath)

# axis labels
plt.xlabel('School')
plt.ylabel('SAT Scores')

# axis tick labels
schools = ['\n'.join(wrap(school, 15)) for school in schools]
plt.xticks(indx, schools)
plt.yticks(np.arange(0, 2400, 2400/len(indx)))

plt.title('Average SAT Scores of NY Public School')
plt.show()
