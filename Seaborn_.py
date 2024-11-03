import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load an example data
data = sns.load_dataset('tips')

# create var chart
sns.barplot(x='day', y='total_bill', data=data)

#customizing the appeatance 
plt.title('Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill')
plt.xticks(rotation=45)

plt.show()


#customize the color
sns.barplot(x='day',y='total_bill',data=data,palette='viridis')

#adding lavels and title
plt.title('Total Bill by Day With Custom Color')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill')

plt.show()

# save the plot to a file 
plt.savefig('bar_chart.png')

