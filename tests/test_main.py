import os
import sys

import pytest
from fastapi.testclient import TestClient

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gacha_logic import RANKS
from main import app

client = TestClient(app)

# Fixtureを定義して、APIリクエストを共通化
@pytest.fixture(scope="module")
def api_response():
    
    #APIにリクエストを送り、そのレスポンスを返すfixture
    return client.get("/gacha")

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

def test_get_non_existent_path_returns_404():
    """
    存在しないパスへのGETリクエストが404を返すことをテストする
    """
    response = client.get("/non-existent-path")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

@pytest.mark.parametrize("method", ["POST", "PUT", "DELETE", "PATCH"])
def test_method_not_allowed_for_gacha_endpoint(method):
    """
    GET以外でのHTTPメソッドが405を返すことをテストする
    """
    # getattrを使って動的にHTTPメソッドを呼び出す
    response = getattr(client, method.lower())("/gacha")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}