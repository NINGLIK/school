import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ["SimHei"]
data = pd.read_excel(r'C:\NINGLIK\school\数据可视化\23-24-2《数据可视化》期中考核数据--人工坐席接听数据.xlsx')

# data_cleaned = data.dropna(subset=['部', '人工服务接听量'])

# # Aggregate the service volumes by department
# service_volumes = data_cleaned.groupby('部')['人工服务接听量'].sum()

# plt.figure(figsize=(10, 6))
# service_volumes.plot(kind='bar', color='skyblue')
# plt.title('Service Volumes by Department')
# plt.xlabel('Department')
# plt.ylabel('Service Volumes')
# plt.xticks(rotation=45)
# plt.tight_layout()
# # plt.savefig('/mnt/data/bar_chart_service_volumes.png')
# plt.show()

# data_cleaned = data.dropna(subset=['班', '呼入通话时长(秒)'])

# avg_call_duration = data_cleaned.groupby('班')['呼入通话时长(秒)'].mean()

# plt.figure(figsize=(10, 6))
# avg_call_duration.plot(kind='line', marker='o', color='green')
# plt.title('Average Call Duration by Shift')
# plt.xlabel('Shift')
# plt.ylabel('Average Call Duration (minutes)')
# plt.grid(True)
# plt.tight_layout()
# # plt.savefig('/mnt/data/line_chart_avg_call_duration.png')
# plt.show()


data_cleaned = data.dropna(subset=['组', '服务评价推送成功数'])
plt.figure(figsize=(10, 6))
sns.boxplot(x='组', y='服务评价推送成功数', data=data_cleaned)
plt.title('Service Evaluation Push Success Count by Group')
plt.xlabel('Group')
plt.ylabel('Push Success Count')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.savefig('/mnt/data/box_plot_push_success_count.png')
plt.show()

