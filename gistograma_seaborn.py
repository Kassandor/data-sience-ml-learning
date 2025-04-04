import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')

ax = sns.histplot(tips['total_bill'], kde=True, cumulative=True)
plt.title('Кумулятивное распределение счетов')
plt.show()