import pytest


@pytest.mark.parametrize("data", [
    {
        "name": "api1",
        "url": "https://example.com/1",
        "method": "POST"
    },
    {
        "name": "api2",
        "url": "https://example.com/2",
        "method": "GET"
    }
])
def test_create_param(client, data):
    res = client.post("/api/create", json=data)

    assert res.status_code == 200