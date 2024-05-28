import random

def shuffle_string(s):
    original = list(s)
    shuffled = original[:]
    random.shuffle(shuffled)
    
    # 如果洗牌后的字符串和原字符串相同，继续洗牌直到不同
    while shuffled == original:
        random.shuffle(shuffled)
    
    return ''.join(shuffled)

# 测试
original_string = "xxyxx"
shuffled_string = shuffle_string(original_string)
print(f"Original: {original_string}")
print(f"Shuffled: {shuffled_string}")
