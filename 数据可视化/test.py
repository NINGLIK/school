import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False


# Correcting the mismatch in array lengths and creating the DataFrame again
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
beijing = [-5, 0, 8, 15, 22, 28, 26, 20, 12, 5, -3, -3]  # Assumed the same value as November for December for Beijing
shanghai = [3, 5, 10, 16, 21, 25, 29, 28, 23, 17, 11, 6]
guangzhou = [13, 15, 18, 23, 27, 30, 33, 32, 28, 22, 17, 14]
chengdu = [6, 8, 13, 18, 22, 25, 28, 27, 22, 16, 10, 7]

# Creating a DataFrame
df_temperatures = pd.DataFrame({
    'Month': months,
    'Beijing': beijing,
    'Shanghai': shanghai,
    'Guangzhou': guangzhou,
    'Chengdu': chengdu
})

# Set Month as index
df_temperatures.set_index('Month', inplace=True)

# Now let's plot the line graph
plt.figure(figsize=(14, 7))

# Plotting each city's temperature trend
for city in df_temperatures.columns:
    plt.plot(df_temperatures.index, df_temperatures[city], label=city, marker='o')

# Adding the title and labels as requested
plt.title('不同城市月平均气温变化对比', fontsize=16)
plt.xlabel('月份', fontsize=14)
plt.ylabel('气温 (°C)', fontsize=14)

# Adding the legend with the title
plt.legend(title='城市', fontsize=12, title_fontsize='13', loc='upper right')

# Showing the plot with grid
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlap
plt.show()
