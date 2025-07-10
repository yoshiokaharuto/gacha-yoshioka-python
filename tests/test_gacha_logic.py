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


