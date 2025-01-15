from datetime import datetime
from typing import Optional
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

    model_config = {
        "from_attributes": True
    }


class ApplicationsInDB(BaseModel):
    id: UUID
    user_name: str
    description: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class ApplicationsGetResponse(BaseModel):
    applications: list[ApplicationsInDB]


class ApplicationKafkaModel(BaseModel):
    id: str
    user_name: str
    description: str
    created_at: datetime


class PaginationSchema(BaseModel):
    page: int = Field(1, ge=1, description="Номер текущей страницы")
    size: int = Field(10, ge=1, description="Количество записей на странице")
    user_name: Optional[str] = Field(None, description="Имя пользователя для фильтрации")
