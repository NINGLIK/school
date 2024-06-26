def solve_chess(t, cases):
    results = []
    for p1, p2, p3 in cases:
        max_draws = -1
        # 遍历所有可能的平局组合
        for x12 in range(p3 + 1):
            for x13 in range(p3 + 1):
                for x23 in range(p3 + 1):
                    # 计算每个玩家必须获胜的场次
                    w12 = (p1 - x12 - x13) / 2
                    w21 = (p2 - x12 - x23) / 2
                    w13 = (p1 - x13 - x12) / 2
                    w31 = (p3 - x13 - x23) / 2
                    w23 = (p2 - x23 - x12) / 2
                    w32 = (p3 - x23 - x13) / 2
                    
                    # 检查计算出的胜利次数是否都是整数且非负
                    if all(w == int(w) and w >= 0 for w in [w12, w21, w13, w31, w23, w32]):
                        # 计算总平局数
                        total_draws = x12 + x13 + x23
                        if total_draws > max_draws:
                            max_draws = total_draws
        
        # 将最大平局数或-1加入结果列表
        results.append(max_draws)
    
    return results

# 测试用例
t = 7
cases = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 1, 1),
    (1, 1, 2),
    (3, 3, 3),
    (3, 4, 5),
    (1, 1, 10)
]

# 调用函数
results = solve_chess(t, cases)
for result in results:
    print(result)
