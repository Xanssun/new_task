from fastapi import APIRouter, Depends, status
from schemas.app_schemas import (ApplicationCreate, ApplicationsCreateResponse,
                                 ApplicationsGetResponse, PaginationSchema)
from services.app_serivces import ApplicationsService, get_applications_service

router = APIRouter(
    tags=['applications'],
)

@router.post(
    "/applications",
    status_code=status.HTTP_201_CREATED,
    description="Создает заявку",
    summary="Создать заявку",
    response_model=ApplicationsCreateResponse,
)
async def create_application(
    app_create: ApplicationCreate,
    app_service: ApplicationsService = Depends(get_applications_service),
) -> ApplicationsCreateResponse:
    application = await app_service.create_application(app_create)
    return application


@router.get(
    "/applications",
    status_code=status.HTTP_200_OK,
    description="Получает заявки",
    summary="Получить заявки",
    response_model=ApplicationsGetResponse,
)
async def get_applications(
    pagination: PaginationSchema = Depends(),
    app_service: ApplicationsService = Depends(get_applications_service),
) -> ApplicationsGetResponse:
    applications = await app_service.get_applications(pagination=pagination)
    return ApplicationsGetResponse(applications=applications)
