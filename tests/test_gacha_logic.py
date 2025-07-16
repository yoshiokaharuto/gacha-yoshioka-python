import sys
import os
import pytest
import math
from collections import Counter
from unittest.mock import patch

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# gacha_logicからRANKS定数とdraw_gacha関数をインポート
from gacha_logic import RANKS, draw_gacha

def test_ranks_probabilities_sum_to_one():
    """
    RANKS定数の確率の合計が1.0であることをテストする
    """
    # 浮動小数点数の比較のため、math.iscloseを使用
    assert math.isclose(sum(RANKS.values()), 1.0)

def test_ranks_probabilities_are_non_negative():
    """
    RANKS定数の全ての確率が0以上であることをテストする
    """
    assert all(prob >= 0 for prob in RANKS.values())

def test_draw_gacha_returns_valid_rank():
    """
    draw_gacha関数が有効なランクを返すことをテストする
    """
    # RANKS定数のキーを有効なランクとして使用
    valid_ranks = set(RANKS.keys())
    result = draw_gacha()
    assert result in valid_ranks

def test_gacha_probability_distribution():
    """
    ガチャの確率分布が期待値に近いことを統計的にテストする
    """
    num_draws = 10000  # 試行回数
    results = [draw_gacha() for _ in range(num_draws)]
    counts = Counter(results)

    # RANKS定数を期待される確率として使用
    expected_probabilities = RANKS

    # 許容誤差
    margin = 0.03

    for rank, expected_prob in expected_probabilities.items():
        actual_prob = counts[rank] / num_draws
        assert expected_prob - margin <= actual_prob <= expected_prob + margin, (
            f"Rank {rank} の排出率が期待値から外れています。"
            f"期待値: {expected_prob}, 実際: {actual_prob}"
        )

@pytest.mark.parametrize("expected_rank", RANKS.keys())
@patch('gacha_logic.random.choices')
def test_draw_gacha_with_mock_parametrized(mock_choices, expected_rank):
    """
    random.choicesをモック化し、指定されたランクが返ることをテストする(パラメタライズ)
    """
    # モックが指定されたランクのリストを返すように設定
    mock_choices.return_value = [expected_rank]

    # draw_gacha() を実行
    result = draw_gacha()

    # 結果が期待したランクと一致することを確認
    assert result == expected_rank

    # random.choicesが期待通りに呼び出されたかを確認
    mock_choices.assert_called_once_with(
        list(RANKS.keys()),
        weights=list(RANKS.values()),
        k=1
    )

