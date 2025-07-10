import random

def draw_gacha():
    """
    排出率
    S: 5%
    A: 15%
    B: 30%
    C: 50%
    """
    ranks = {
        "S": 0.05,
        "A": 0.15,
        "B": 0.30,
        "C": 0.50,
    }
    
    # 重み付きランダム選択
    # 第一引数: 選択肢のリスト(今回はranksのキー)
    # 第二引数: 各選択肢の重み（確率)(ranksのvalue）)
    # 第三引数: 選択する個数
    # k=1は1つの要素を選ぶこと
    result = random.choices(list(ranks.keys()), weights=list(ranks.values()), k=1)
    
    return result[0]

if __name__ == '__main__':
    print(draw_gacha())
