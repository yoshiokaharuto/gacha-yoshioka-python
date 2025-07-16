import pytest
from fastapi.testclient import TestClient
import sys
import os

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from gacha_logic import RANKS

client = TestClient(app)

# Fixtureを定義して、APIリクエストを共通化
@pytest.fixture(scope="module")
def api_response():
    
    #APIにリクエストを送り、そのレスポンスを返すfixture
    return client.get("/")

def test_read_main_returns_200_ok(api_response):
    
    #ステータスコード200を返すことをテストする
    assert api_response.status_code == 200

def test_read_main_response_has_result_key(api_response):
    
    #レスポンスのJSONに"result"キーが存在することをテストする
    assert "result" in api_response.json()

def test_read_main_result_is_valid_rank(api_response):
    
    #レスポンスの"result"の値が有効なランクであることをテストする
    data = api_response.json()
    assert data["result"] in RANKS.keys()