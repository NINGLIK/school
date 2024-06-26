def function(NumberOfPeople, bestFriend):
    minloop = float('inf')  # 使用无限大来初始化最小循环
    for topeople in range(len(NumberOfPeople)):
        var = topeople
        tiaochubianliang = False
        arr = []
        arr.append(NumberOfPeople[var])
        for _ in range(len(NumberOfPeople)):
            next_person = bestFriend[NumberOfPeople[var] - 1] - 1
            arr.append(NumberOfPeople[next_person])
            var = next_person
            if arr.count(NumberOfPeople[next_person]) > 1:
                tiaochubianliang = True
                break
        if tiaochubianliang:
            cycle_length = len(arr) - 1
            if minloop > cycle_length:
                minloop = cycle_length

    return minloop


NumberOfTests = int(input())
for _ in range(NumberOfTests):
    NumberOfPeople = list(range(1, int(input()) + 1))
    bestFriend = [int(x) for x in input().split()]
    print(function(NumberOfPeople, bestFriend))
