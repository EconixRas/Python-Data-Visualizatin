import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv

df = read_csv('bike sharing.csv')
df = df[['mnth', 'yr', 'casual', 'registered']] # only extract the columns we need
df = df[(df['mnth'].isin([1, 2, 3])) & (df['yr']==0)] # Jan, Feb, and Mar data of first year

x = 'mnth' 
y = 'casual'

plt.figure(figsize=(7,7,))
ax = sns.boxplot(x=x, y=y, data=df)
ax = sns.swarmplot(x=x, y=y, data=df, color='grey')
plt.show()
