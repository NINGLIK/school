import matplotlib.pyplot as plt


plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False

# Data from the table
categories = ["玩具文娱", "童车童床", "孕妈专区", "春夏新品", "宝宝尿裤", "洗护喂养", "奶粉辅食", "童鞋", "童装"]
sales = [39670, 4135.8, 5292.5, 6240.8, 6543.5, 6633.6, 7414.5, 8308.2, 30353]

# Create a pie chart
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title("某平台子类目的销售额")

# Adjust the legend to display in two columns
plt.legend(title="子类目", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), ncol=2)

# Add a table displaying the sales data
table_data = [[cat, f"{sal:.1f}亿"] for cat, sal in zip(categories, sales)]
table = plt.table(cellText=table_data, colLabels=["子类目", "销售额（亿）"], loc="bottom", cellLoc='center', colWidths=[0.15, 0.15])

# Adjust layout to make room for the table
plt.subplots_adjust(left=0.2, bottom=0.2)

# Display the plot
plt.show()
