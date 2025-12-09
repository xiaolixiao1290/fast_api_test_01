from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "欢迎使用 FastAPI"}


@app.get("/current_time")
def get_current_time():
    now = datetime.now()
    formatted_time = now.strftime("%Y年%m月%d日%H:%M:%S")
    return {
        "current_time": formatted_time,
        "timestamp": now.timestamp()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

