import random

def shuffle_string(s):
    original = list(s)
    shuffled = original[:]
    random.shuffle(shuffled)
    
    # 如果洗牌后的字符串和原字符串相同，继续洗牌直到不同
    while shuffled == original:
        random.shuffle(shuffled)
    
    return ''.join(shuffled)

def fuciton(characterString):
    i : int = 0
    while i < len(characterString) - 1:
        if(characterString[i] != characterString[i + 1]):
            return 1
        i += 1
    return 0

data = int(input())
for _ in range(data):
    characterString = input()
    result=fuciton(characterString)
    if(result==1):
        print('YES')
        print(shuffle_string(characterString))
    else:
        print('NO')
