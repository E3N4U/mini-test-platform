import requests
import json
from app.database import SessionLocal
from app.models import TestCase, API
from runner.assertion import assert_response
def run_tests():
    db = SessionLocal()
    results = []

    cases = db.query(TestCase).all()

    for case in cases:
        api = db.query(API).filter(API.id == case.api_id).first()

        input_data = json.loads(case.input_data)
        expected = json.loads(case.expected)

        try:
            if api.method == "GET":
                r = requests.get(api.url, params=input_data)
            else:
                r = requests.post(api.url, json=input_data)

            assert_result = assert_response(r, expected)

            results.append({
                "case_id": case.id,
                "passed": assert_result["passed"],
                "errors": assert_result["errors"],
                "response": r.text
            })


        except Exception as e:
            results.append({
                "case_id": case.id,
                "passed": False,
                "error": str(e)
            })

    return results