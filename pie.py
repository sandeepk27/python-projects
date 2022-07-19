import seaborn as sns
import matplotlib.pyplot as plt
data = [10, 21, 30, 27, 12]
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']

colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
plt.show()
