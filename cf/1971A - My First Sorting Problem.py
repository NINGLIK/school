def function(number1, number2):
    if number1 > number2:
        number1, number2 = number2, number1
    return number1, number2

data = int(input())
for i in range(data):
    user_input = input()
    num1, num2 = map(int, user_input.split())
    result = function(num1, num2)
    print(f"{result[0]} {result[1]}")