import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

ax = sns.barplot(x="day", y="total_bill", hue='smoker', data=tips)
plt.title("Средний счет по дням недели для курящих и некурящих")
plt.show()