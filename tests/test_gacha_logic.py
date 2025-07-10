import sys
import os
import pytest
from collections import Counter

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gacha_logic import draw_gacha

def test_draw_gacha_returns_valid_rank():
    """
    draw_gacha関数が有効なランクを返すことをテストする
    """
    valid_ranks = {"S", "A", "B", "C"}
    result = draw_gacha()
    assert result in valid_ranks

def test_gacha_probability_distribution():
    """
    ガチャの確率分布が期待値に近いことを統計的にテストする
    """
    num_draws = 10000  # 試行回数
    results = [draw_gacha() for _ in range(num_draws)]
    counts = Counter(results)

    expected_probabilities = {
        "S": 0.05,
        "A": 0.15,
        "B": 0.30,
        "C": 0.50,
    }

    # 許容誤差
    # 試行回数が多ければもっと小さくできる
    margin = 0.03  

    for rank, expected_prob in expected_probabilities.items():
        actual_prob = counts[rank] / num_draws
        assert expected_prob - margin <= actual_prob <= expected_prob + margin, (
            f"Rank {rank} の排出率が期待値から外れています。"
            f"期待値: {expected_prob}, 実際: {actual_prob}"
        )

