import random

# ガチャの排出率を定数として定義
RANKS = {
    "S": 0.05,
    "A": 0.15,
    "B": 0.30,
    "C": 0.50,
}

def draw_gacha():
    """
    ガチャを引き、結果のランクを返す。
    排出率はRANKS定数に基づく。
    """
    # 重み付きランダム選択
    # 第一引数: 選択肢のリスト(今回はRANKSのキー)
    # 第二引数: 各選択肢の重み（確率）のリスト(今回はRANKSの値）)
    # 第三引数: 選択する個数
    # k=1は1つの要素を選ぶことを意味する
    result = random.choices(list(RANKS.keys()), weights=list(RANKS.values()), k=1)
    
    return result[0]

if __name__ == '__main__':
    print(draw_gacha())
