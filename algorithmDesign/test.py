from pulp import LpProblem, LpMaximize, LpVariable

# 创建线性规划问题
prob = LpProblem("MaximizeZero", LpMaximize)

# 定义决策变量
x = LpVariable("Chickens", lowBound=0, cat="Integer")  # 鸡的数量
y = LpVariable("Rabbits", lowBound=0, cat="Integer")   # 兔子的数量

# 定义目标函数（最大化0）
prob += 0, "MaximizeZero"

# 添加约束条件
prob += x + y == 35  # 总头数为35
prob += 2*x + 4*y == 94  # 总腿数为94

# 求解问题
prob.solve()

# 打印结果
print("Optimal solution:")
print("Chickens =", x.varValue)
print("Rabbits =", y.varValue)
