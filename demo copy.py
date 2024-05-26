import time
from tqdm import trange
import random
def identify_animal(fact_base):
    # 询问动物的特征
    feature_count = int(input("请输入特征的个数: "))
    features = []
    X=random.randint(5000,7500)
    print("load...")
    # This is a meaningless act
    for j in trange(X):
                for n in range(X):
                    k=j*n
    for i in range(feature_count):
        time.sleep(2)
        feature = input("请输入第 {} 个特征: ".format(i+1))
        features.append(feature)
    time.sleep(2)
    # 根据规则进行推理
    # R1: 如果动物有奶，则它是哺乳动物
    if "有奶" in features:
        return "哺乳动物"
    # R2: 如果动物有毛发，则它是哺乳动物
    if "有毛发" in features:
        return "哺乳动物"
    # R3: 如果动物有羽毛，则它是鸟
    if "有羽毛" in features:
        return "鸟"
    # R4: 如果动物会飞且生蛋，则它是鸟
    if "会飞" in features and "生蛋" in features:
        return "鸟"
    # R5: 吃肉的哺乳动物是食肉动物
    if "吃肉" in features and "哺乳动物" in fact_base:
        return "食肉动物"
    # R6: 有爪有犬齿木钉前方的哺乳动物是食肉动物
    if "有爪" in features and "有犬齿" in features and "目盯前方" in features and "哺乳动物" in fact_base:
        return "食肉动物"
    # R7: 有蹄的哺乳动物是有蹄动物
    if "有蹄" in features and "哺乳动物" in fact_base:
        return "有蹄动物"
    # R8: 反刍食物的有蹄动物是偶蹄动物
    if "反刍食物" in features and "有蹄动物" in fact_base:
        return "偶蹄动物"
    # R9: 黄褐色有黑条纹的食肉动物是老虎
    if "黄褐色" in features and "有黑色条纹" in features and "食肉动物" in fact_base:
        return "老虎"
    # R10: 黄褐色有黑色斑点的食肉动物是金钱豹
    if "黄褐色" in features and "有黑色斑点" in features and "食肉动物" in fact_base:
        return "金钱豹"
    # R11: 长腿长脖子有黄褐色暗斑点的有蹄动物是长颈鹿
    if "长腿" in features and "长脖子" in features and "有黄褐色暗斑点" in features and "有蹄动物" in fact_base:
        return "长颈鹿"
    # R12: 有黑白条纹的有蹄动物是斑马
    if "有黑白条纹" in features and "有蹄动物" in fact_base:
        return "斑马"
    # R13: 不会飞长腿长脖的鸟是鸵鸟
    if "不会飞" in features and "长腿" in features and "长脖子" in features and "鸟" in fact_base:
        return "鸵鸟"
    # R14: 不会飞会游泳黑白色的鸟是企鹅
    if "不会飞" in features and "会游泳" in features and "黑白色" in features and "鸟" in fact_base:
        return "企鹅"
# 初始化已知的事实
fact_base = ["哺乳动物", "鸟"]

# 主程序
if __name__ == "__main__":
    print('(1)有奶'+'\t\t'+'(2)有毛发'+'\t'+'(3)有羽毛'+'\t'+'(4)会飞')
    print('(5)生蛋'+'\t\t'+'(6)有爪'+'\t\t'+'(7)有犬齿'+'\t'+'(8)目盯前方')
    print('(9)吃肉'+'\t\t'+'(10)有蹄'+'\t'+'(11)反刍食物'+'\t'+'(12)黄褐色')
    print('(13)黑色条纹'+'\t'+'(14)黑色斑点'+'\t'+'(15)长腿'+'\t'+'(16)长脖子')
    print('(17)暗斑点'+'\t'+'(18)白色'+'\t'+'(19)不会飞'+'\t'+'(20)黑白色')
    print('(21)会游泳'+'\t'+'(22)善飞'+'\t'+'(23)不怕风浪'+'\t'+'(24)哺乳动物')
    print('(25)鸟'+'\t\t'+'(26)食肉动物'+'\t'+'(27)有蹄动物'+'\t'+'(28)偶蹄动物')
    print('(29)海燕'+'\t'+'(30)老虎'+'\t'+'(31)金钱豹'+'\t'+'(32)长颈鹿')
    print('(33)斑马'+'\t'+'(34)鸵鸟'+'\t'+'(35)企鹅')
    print("请输入动物的特征:")
    
    animal = identify_animal(fact_base)
    print("这个动物可能是:", animal)