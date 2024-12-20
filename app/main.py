from fastapi import FastAPI
from app.routers import ci_cd_routes

app = FastAPI(title="CI/CD Automation Server")

# Подключаем маршруты
app.include_router(ci_cd_routes.router)

@app.get("/")
async def read_root() -> dict:
    """Корневой маршрут, возвращающий приветственное сообщение."""
    return {"message": "Добро пожаловать на сервзер автоматизации CI/CD!"}