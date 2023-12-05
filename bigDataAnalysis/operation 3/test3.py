import pandas as pd
import numpy as np
# (1) 读取文件test2.xlsx中的数据，用一个数据框变量df进行引用
df = pd.read_excel(r'/home/ninglik/ninglik/codes/school/bigDataAnalysis/operation 2/test2.xlsx')
# (2) 对数据框变量df进行切片操作，选取第3列、第4列，
# 切片后得到一个新的数据框df1，
# 并将df1转换为Numpy数组Nt
df1 = df.iloc[:, 2:4]
Nt = df1.to_numpy()
print(df1)
print("~"*50)
print(Nt)
# (3) 基于df第2列，构造一个逻辑数组TF，即满足交易日期小于等于2017-01-16且大于等于2017-01-05为真，否则为假
TF = (df.iloc[:, 1] >= '2017-01-05') & (df.iloc[:, 1] <= '2017-01-16')
print(TF)
# (4) 以逻辑数组TF为行索引，取数组Nt中的第2列交易量数据并求和，记为S
S = Nt[TF, 1].sum()
print(S)