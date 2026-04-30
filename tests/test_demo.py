import os
import allure
import pytest

LANG = os.getenv("LANGUAGE", "zh")

def t(zh, en):
    return zh if LANG == "zh" else en


@allure.feature(t("接口测试", "API Test"))
@allure.story(t("访问创建接口", "Create API endpoint"))
def test_create(client):

    data = {"key": "value"}

    with allure.step(t("发送请求", "Send request")):
        res = client.post("/api/create", json=data)

        allure.attach(
            str(res.json()),
            name="response body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step(t("校验状态码", "Check status code")):
        assert res.status_code == 200


@pytest.mark.parametrize("data", [
    {"key": "value"},
    {"key": "test"}
])
def test_create_param(client, data):
    res = client.post("/api/create", json=data)

    assert res.status_code == 200
    assert "key" in res.json()