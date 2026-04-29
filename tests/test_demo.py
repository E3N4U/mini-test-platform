import requests

def test_health():
    r = requests.get("http://127.0.0.1:8000/docs")
    assert r.status_code == 200