from fastapi import Depends
from infra.postgres import get_session
from models.entities import Application
from schemas.app_schemas import ApplicationCreate
from sqlalchemy.ext.asyncio import AsyncSession


class ApplicationsService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


    async def create_applications(self, application_create: ApplicationCreate):
        application = Application(**application_create.model_dump())
        self.db_session.add(application)
        await self.db_session.commit()
        await self.db_session.refresh(application)

        return application

    async def get_applications(self):
        ...


def get_applications_service(
    db_session: AsyncSession = Depends(get_session),
):
    return ApplicationsService(db_session=db_session)
