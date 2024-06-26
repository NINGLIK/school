import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ["SimHei"]

# 创建数据表
data = {
    '性别': ['男', '女'],
    '6岁及以上人口': [49290, 48114],
    '未上过学': [1267, 3370],
    '小学': [11416, 13491],
    '初中': [18816, 15973],
    '高中': [8492, 6430],
    '大学专科': [4615, 4550],
    '大学本科': [4317, 3880],
    '研究生': [367, 420]
}
df = pd.DataFrame(data)

# 受教育程度分类
education_levels = ['未上过学', '小学', '初中', '高中', '大学专科', '大学本科', '研究生']

# 按性别和受教育程度统计人数
education_counts = df.set_index('性别')[education_levels]

# 设置颜色
colors = plt.cm.viridis(np.linspace(0, 1, len(education_levels)))

# 绘制图表
fig = plt.figure(figsize=(18, 10))
grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.4)

# 男生柱形图
ax1 = fig.add_subplot(grid[0, 0])
education_counts.loc['男'].plot(kind='bar', ax=ax1, color=colors)
ax1.set_title('男生受教育程度对比')
ax1.set_xlabel('受教育程度')
ax1.set_ylabel('人数')

# 圆环图
ax3 = fig.add_subplot(grid[0, 1])
total_counts = education_counts.sum(axis=0)
total_counts.plot(kind='pie', ax=ax3, autopct='%1.1f%%', startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.3), colors=colors)
ax3.set_title('不同性别受教育程度占比')
ax3.set_ylabel('')

# 玫瑰图
ax4 = fig.add_subplot(grid[1, 0], polar=True)
theta = np.linspace(0.0, 2 * np.pi, len(total_counts), endpoint=False)
radii = total_counts.values
width = 2 * np.pi / len(total_counts)

bars = ax4.bar(theta, radii, width=width, bottom=0.0, color=colors)
ax4.set_xticks(theta)
ax4.set_xticklabels(total_counts.index)

ax4.set_title('不同性别受教育程度玫瑰图')

# 女生柱形图
ax2 = fig.add_subplot(grid[1, 1])
education_counts.loc['女'].plot(kind='bar', ax=ax2, color=colors)
ax2.set_title('女生受教育程度对比')
ax2.set_xlabel('受教育程度')
ax2.set_ylabel('人数')

# 显示图表
plt.show()
