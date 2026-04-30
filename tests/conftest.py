import pytest
from fastapi.testclient import TestClient
from app.main import app

# 全局 client（所有测试可复用）
@pytest.fixture
def client():
    return TestClient(app)