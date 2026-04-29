# 🚀 Mini Test Platform（接口自动化测试平台）

一个基于 **FastAPI + SQLAlchemy** 构建的轻量级接口自动化测试平台，支持接口管理、测试用例管理以及自动化执行与断言。

---

## 📌 项目背景

在接口测试过程中，常见问题包括：

* 测试用例分散，难以管理
* 手动执行效率低
* 缺乏统一断言机制

本项目实现了一个**最小可用测试平台（MVP）**，用于解决上述问题，并具备向企业级测试平台扩展的能力。

---

## 🧱 技术栈

* **后端框架**：FastAPI
* **ORM**：SQLAlchemy
* **数据库**：SQLite（可扩展 MySQL）
* **HTTP请求**：requests
* **测试框架**：pytest（可扩展）
* **运行服务**：uvicorn

---

## ✨ 功能特性

### ✅ 接口管理

* 创建接口（URL、请求方法）
* 支持 HTTP 请求配置

### ✅ 测试用例管理

* 关联接口创建测试用例
* 支持输入参数（JSON）
* 支持期望结果定义

### ✅ 自动化执行

* 批量执行测试用例
* 自动发送 HTTP 请求
* 返回执行结果

### ✅ 断言引擎（已升级）

支持多维度断言：

* 状态码校验
* JSON 字段校验（支持嵌套路径，如 `json.key`）
* 多断言组合
* 错误信息输出

示例：

```json
{
  "status_code": 200,
  "json": {
    "json.key": "value"
  }
}
```

---

## 📂 项目结构

```
mini-test-platform/
├── app/                # FastAPI 应用
│   ├── main.py
│   ├── models.py
│   └── database.py
├── runner/             # 执行引擎
│   ├── runner.py
│   └── assertion.py
├── tests/              # 示例测试
├── requirements.txt
└── README.md
```

---

## ⚙️ 本地运行

### 1️⃣ 克隆项目

```bash
git clone https://github.com/你的用户名/mini-test-platform.git
cd mini-test-platform
```

---

### 2️⃣ 创建虚拟环境

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

---

### 4️⃣ 启动服务

```bash
python -m uvicorn app.main:app --reload
```

---

### 5️⃣ 打开接口文档

```
http://127.0.0.1:8000/docs
```

---

## 🧪 使用流程

1. 创建接口 `/api/create`
2. 创建测试用例 `/case/create`
3. 执行测试 `/run`
4. 查看结果（是否通过 + 错误信息）

---

## 📊 示例执行结果

```json
[
  {
    "case_id": 1,
    "passed": true,
    "errors": [],
    "response": "..."
  }
]
```

---

## 🚀 可扩展方向（重点）

本项目可进一步扩展为企业级测试平台：

* 🔹 支持正则断言 / 包含断言
* 🔹 集成 Allure 测试报告
* 🔹 接入 CI/CD（GitHub Actions）
* 🔹 支持环境变量（测试/生产）
* 🔹 支持数据库切换（MySQL/PostgreSQL）
* 🔹 UI 前端（Vue/React）

---

## 🎯 项目价值

* 从 0 构建测试平台核心能力
* 理解接口自动化测试流程
* 掌握断言引擎设计
* 具备向企业级测试平台扩展能力

---

## 👤 作者

* GitHub: https://github.com/E3N4U

---

## 📄 License

MIT License
