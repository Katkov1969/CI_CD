from pydantic import BaseModel

class CIcdRequest(BaseModel):
    """Модель данных для запроса CI/CD."""
    project_name: str
    tools: list[str]

class CIcdResponse(BaseModel):
    """Модель данных для ответа CI/CD."""
    project_name: str
    status: str
    message: str