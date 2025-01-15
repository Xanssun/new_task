from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    ...


class ApplicationsCreateResponse(BaseModel):
    ...


class ApplicationsGetResponse(BaseModel):
    ...


class PaginationSchema(BaseModel):
    page: int = Field(1, ge=1, description="Номер текущей страницы")
    size: int = Field(10, ge=1, description="Количество записей на странице")
