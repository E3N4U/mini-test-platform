import json

def get_value_by_path(data, path):
    """
    支持 a.b.c 形式的JSON路径
    """
    keys = path.split(".")
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data


def assert_response(response, expected):
    """
    核心断言逻辑
    """
    result = {
        "passed": True,
        "errors": []
    }

    # 1️⃣ 状态码校验
    if "status_code" in expected:
        if response.status_code != expected["status_code"]:
            result["passed"] = False
            result["errors"].append(
                f"status_code expected {expected['status_code']} but got {response.status_code}"
            )

    # 2️⃣ JSON字段校验
    if "json" in expected:
        try:
            resp_json = response.json()
        except:
            result["passed"] = False
            result["errors"].append("response is not valid JSON")
            return result

        for path, exp_value in expected["json"].items():
            actual_value = get_value_by_path(resp_json, path)

            if actual_value != exp_value:
                result["passed"] = False
                result["errors"].append(
                    f"{path} expected {exp_value} but got {actual_value}"
                )

    return result