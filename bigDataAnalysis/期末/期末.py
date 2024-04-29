import numpy as np
import pandas as pd


def gcd(a, b):
    """
    计算两个数的最大公约数

    Parameters:
    - a:公约数a
    - b:公约数b
    
    Returns:
    - a:最大公约数
    """
    while b:
        a, b = b, a % b
    return a

# num1 = 48
# num2 = 18
# result = gcd(num1, num2)
# print(f"{num1} 和 {num2} 的最大公约数是: {result}")

def calculate_distance(point_a, point_b):
    """
    计算两点之间的欧几里德距离

    Parameters:
    - point_a: 第一个点的坐标，例如 [x1, y1]
    - point_b: 第二个点的坐标，例如 [x2, y2]

    Returns:
    - distance: 两点之间的距离
    """
    point_a = np.array(point_a)
    point_b = np.array(point_b)
    distance = np.linalg.norm(point_a - point_b)
    return distance
# point1 = [1, 2]
# point2 = [4, 6]
# result = calculate_distance(point1, point2)
# print(f"两点之间的距离为: {result}")

def comput(r,h):
    S=(2 * 3.14 * r**2) + (2 * 3.14 * r * h)
    V=3.14 * r** 2 * h
    return S,V

# r=10
# h=11
# result = comput(r, h)
# print(f"圆柱体的表面积为: {result[0]}")
# print(f"圆柱体的体积为: {result[1]}")
def xiaohong():    
    # (1) 读取文件test1.txt中的4位同学的成绩，用一个数据框变量df进行引用
    df = pd.read_csv(r'C:\NINGLIK\school\bigDataAnalysis\期末\test1.txt', delimiter=',')

    # (2) 对数据框变量df进行切片操作，分别获得小红、张明、小江和小李的各科成绩
    df1 = df[df['姓名'] == '小红']
    df2 = df[df['姓名'] == '张明']
    df3 = df[df['姓名'] == '小江']
    df4 = df[df['姓名'] == '小李']

    # (3) 将成绩列转换为数值类型
    df['成绩'] = pd.to_numeric(df['成绩'], errors='coerce')

    # (4) 利用数据框聚合方法，计算每个同学各科成绩的平均分
    M1 = df1.groupby('姓名')['成绩'].mean()
    M2 = df2.groupby('姓名')['成绩'].mean()
    M3 = df3.groupby('姓名')['成绩'].mean()
    M4 = df4.groupby('姓名')['成绩'].mean()

    # 打印结果
    print("df1:\n", df1)
    print("df2:\n", df2)
    print("df3:\n", df3)
    print("df4:\n", df4)
    print("M1:\n", M1)
    print("M2:\n", M2)
    print("M3:\n", M3)
    print("M4:\n", M4)
xiaohong()