import os
import allure
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

LANG = os.getenv("LANGUAGE", "zh")

def t(zh, en):
    return zh if LANG == "zh" else en

@allure.feature(t("接口测试", "API Test"))
@allure.story(t("访问文档接口", "Access docs endpoint"))
def test_docs():
    with allure.step(t("发送请求", "Send request")):
        res = client.get("/docs")

    with allure.step(t("校验状态码", "Check status code")):
        assert res.status_code == 200