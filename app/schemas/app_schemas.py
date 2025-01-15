from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    user_name: str
    description: str


class ApplicationsCreateResponse(BaseModel):
    id: UUID
    user_name: str
    description: str
    created_at: datetime


class ApplicationsGetResponse(BaseModel):
    ...


class PaginationSchema(BaseModel):
    page: int = Field(1, ge=1, description="Номер текущей страницы")
    size: int = Field(10, ge=1, description="Количество записей на странице")
