from fastapi import Depends
from infra.postgres import get_session
from models.entities import Application
from schemas.app_schemas import (ApplicationCreate, ApplicationsCreateResponse,
                                 ApplicationsInDB, PaginationSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ApplicationsService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_application(self, application_create: ApplicationCreate) -> ApplicationsCreateResponse:
        application = Application(**application_create.model_dump())

        self.db_session.add(application)
        await self.db_session.commit()
        await self.db_session.refresh(application)
        

        return ApplicationsCreateResponse.model_validate(application)

    async def get_applications(self, pagination: PaginationSchema) -> list[ApplicationsInDB]:
        query = select(Application)

        if pagination.user_name:
            query = query.where(Application.user_name.ilike(f"%{pagination.user_name}%"))

        query = query.offset((pagination.page - 1) * pagination.size).limit(pagination.size)

        result = await self.db_session.execute(query)
        applications = result.scalars().all()

        return [ApplicationsInDB.model_validate(app) for app in applications]


def get_applications_service(db_session: AsyncSession = Depends(get_session)):
    return ApplicationsService(db_session=db_session)
