from fastapi import APIRouter
from app.models.ci_cd_models import CIcdRequest, CIcdResponse
from app.services.ci_cd_service import process_ci_cd

router = APIRouter()

@router.post("/ci_cd", response_model=CIcdResponse)
async def create_ci_cd(request: CIcdRequest) -> CIcdResponse:
    """Маршрут для обработки запроса на автоматизацию CI/CD."""
    result = await process_ci_cd(request)
    return result