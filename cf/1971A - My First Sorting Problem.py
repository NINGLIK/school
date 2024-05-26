def function(number1, number2):
    if number1 > number2:
        # 交换 number1 和 number2 的值
        number1, number2 = number2, number1
    return number1, number2

# 提示用户输入总的输入次数
data = int(input())

# 循环输入数据并处理
for i in range(data):
    user_input = input()
    num1, num2 = map(int, user_input.split())
    result = function(num1, num2)
    print(f"{result[0]} {result[1]}")