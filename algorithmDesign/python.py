import pulp

# 定义问题
problem = pulp.LpProblem("P_median_problem", pulp.LpMinimize)

# 定义数据结构
costs = [
    [30, 45, 48, 10, 35],  # C1 客户到设施的成本矩阵
    [25, 60, 70, 35, 50],  # C2
    [28, 15, 25, 32, 10],  # C3
    [45, 30, 20, 24, 12],  # C4
    [58, 12, 25, 60, 30],  # C5
    [65, 30, 15, 57, 33]   # C6
]
demands = [10, 6, 11, 25, 15, 13]  # 每个客户的需求量

num_customers = len(costs)  # 客户数量
num_facilities = len(costs[0])  # 设施数量
num_to_select = 2  # 要选择的中位数数量

# 决策变量
# x[i, j] = 1 表示客户 i 被分配到设施 j，0 表示没有被分配
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_customers) for j in range(num_facilities)), cat='Binary')
# y[j] = 1 表示设施 j 被选为分配中心，0 表示不选
y = pulp.LpVariable.dicts("y", (j for j in range(num_facilities)), cat='Binary')

# 目标函数
# 最小化总成本
problem += pulp.lpSum(demands[i] * costs[i][j] * x[(i, j)] for i in range(num_customers) for j in range(num_facilities))

# 约束条件
# 每个客户必须被分配到一个设施
for i in range(num_customers):
    problem += pulp.lpSum(x[(i, j)] for j in range(num_facilities)) == 1

# 每个设施最多服务 num_to_select 个客户
for j in range(num_facilities):
    for i in range(num_customers):
        problem += x[(i, j)] <= y[j]

# 选择恰好 num_to_select 个设施作为分配中心
problem += pulp.lpSum(y[j] for j in range(num_facilities)) == num_to_select

# 求解问题
problem.solve()

# 输出结果
print("分配中心的位置是:")
for j in range(num_facilities):
    if y[j].varValue > 0.5:
        print(f"D{j+1}", end=" ")
print("\n客户的分配情况是:")
for i in range(num_customers):
    for j in range(num_facilities):
        if x[(i, j)].varValue > 0.5:
            print(f"C{i+1} -> D{j+1}")
