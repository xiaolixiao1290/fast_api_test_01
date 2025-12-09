# FastAPI 最简项目

一个简单的 FastAPI 项目，提供获取当前时间的接口。

## 功能

- 根路由：返回欢迎消息
- 时间接口：返回当前时间（格式：2025年12月09日15:18:44）

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行项目

### 方式1：直接运行（推荐）

```bash
python main.py
```

### 方式2：使用 uvicorn 命令

```bash
# 开发环境（热重载）
uvicorn main:app --reload

# 生产环境
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 访问接口

服务启动后，可以访问以下地址：

- **首页**: http://127.0.0.1:8000/
- **时间接口**: http://127.0.0.1:8000/current_time
- **API 文档**: http://127.0.0.1:8000/docs
- **ReDoc 文档**: http://127.0.0.1:8000/redoc

## API 示例

### 获取当前时间

**请求：**
```
GET http://127.0.0.1:8000/current_time
```

**响应：**
```json
{
  "current_time": "2025年12月09日15:18:44",
  "timestamp": 1733731124.123456
}
```

## 项目结构

```
fast_api_test_01/
├── main.py              # FastAPI 应用主文件
├── requirements.txt     # 项目依赖
└── README.md           # 项目说明
```

## 技术栈

- Python 3.7+
- FastAPI 0.109.0
- Uvicorn 0.27.0

