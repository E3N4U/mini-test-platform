import os
import allure

LANG = os.getenv("LANGUAGE", "zh")

# 中英切换函数
def t(zh, en):
    return zh if LANG == "zh" else en


@allure.feature(t("接口测试", "API Test"))
@allure.story(t("访问文档接口", "Access docs endpoint"))
def test_docs(client):

    with allure.step(t("发送请求", "Send request")):
        res = client.get("/docs")

        # 👉 把响应写入报告（加分点）
        allure.attach(
            res.text,
            name="response body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step(t("校验状态码", "Check status code")):
        assert res.status_code == 200


# 👉 参数化测试（加分项）
import pytest

@pytest.mark.parametrize("data", [
    {"key": "value"},
    {"key": "test"}
])
def test_post(client, data):
    res = client.post("https://httpbin.org/post", json=data)

    assert res.status_code == 200
    assert res.json()["json"] == data