import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

ax = sns.scatterplot(x='total_bill', y='tip', hue='time', data=tips)
plt.title('Связь между счетом и чаевыми в зависимости от времени посещения')
plt.show()