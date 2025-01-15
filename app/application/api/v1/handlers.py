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
async def create_appplications(
    app_create: ApplicationCreate,
    app_service: ApplicationsService = Depends(get_applications_service),
):
    ...


@router.get(
    "/applications",
    status_code=status.HTTP_200_OK,
    description="Получает заявку",
    summary="Получить заявку",
    response_model=ApplicationsGetResponse,
)
async def get_transactions(
    pagination: PaginationSchema,
    app_service: ApplicationsService = Depends(get_applications_service),
):
    ...
