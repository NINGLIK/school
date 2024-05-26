import time
import random
from tqdm import trange
from colorama import Fore, Style

def identify_animal(features):  
    # 定义规则字典，键是特征元组，值是动物分类  
    rules = {  
        ("有奶",): "哺乳动物",  
        ("有毛发",): "哺乳动物",  
        ("有羽毛"): "鸟",  
        ("有羽毛", "生蛋"): "鸟",  
        ("吃肉", "哺乳动物"): "食肉动物",  
        ("有爪", "有犬齿", "目盯前方", "哺乳动物"): "食肉动物",  
        ("有蹄", "哺乳动物"): "有蹄动物",  
        ("反刍食物", "有蹄动物"): "偶蹄动物",  
        ("黄褐色", "有黑色条纹", "食肉动物"): "老虎",  
        ("黄褐色", "有黑色斑点", "食肉动物"): "金钱豹",  
        ("长腿", "长脖子", "黄褐色", "有暗斑点", "有蹄动物"): "长颈鹿",  
        ("有黑白条纹", "有蹄动物"): "斑马",  
        ("不会飞", "长腿", "长脖子", "鸟"): "鸵鸟",  
        ("不会飞", "会游泳", "黑白色", "鸟"): "企鹅"  
    }  
      
    # 检查每个规则的条件是否全部满足  
    for rule_features, animal in rules.items():  
        if all(feature in features for feature in rule_features):  
            return animal  
    # 如果没有匹配到任何规则，返回未知动物
    return "未知动物"

def print_menu():
    print(Fore.BLUE + "="*70)
    print("选择您觉得符合的特征（输入编号，逗号分隔，按回车确认）:")
    print("(1)有奶\t\t(2)有毛发\t(3)有羽毛\t(4)会飞")
    print("(5)生蛋\t\t(6)有爪\t\t(7)有犬齿\t(8)目盯前方")
    print("(9)吃肉\t\t(10)有蹄\t(11)反刍食物\t(12)黄褐色")
    print("(13)黑色条纹\t(14)黑色斑点\t(15)长腿\t(16)长脖子")
    print("(17)暗斑点\t(18)白色\t(19)不会飞\t(20)黑白色")
    print("(21)会游泳\t(22)善飞\t(23)不怕风浪\t(24)哺乳动物")
    print("(25)鸟\t\t(26)食肉动物\t(27)有蹄动物\t(28)偶蹄动物")
    print("(29)海燕\t(30)老虎\t(31)金钱豹\t(32)长颈鹿")
    print("(33)斑马\t(34)鸵鸟\t(35)企鹅")
    print("="*70)
    print(Style.RESET_ALL)


# 示例用法  
if __name__ == "__main__":  
    print_menu()
    feature_count = int(input("请输入特征的个数: "))
    X=random.randint(5000,7500)
    print("加载数据集...")
    # This is a meaningless act
    for j in trange(X):
                for n in range(X):
                    k=j*n
    # features = []
    # 使用集合来存储特征，以自动去重 
    features = set()
    # while True:  
    #     feature = input().strip()  
    #     if feature.lower() == '完成':  
    #         break
    #     features.add(feature)  
    for i in range(feature_count):
        time.sleep(2)
        feature = input("请输入第 {} 个特征: ".format(i+1)).strip()  
        features.add(feature)
    animal = identify_animal(features)  
    print("这个动物可能是:", Fore.GREEN +animal)
    print(Style.RESET_ALL)