from fastapi import Depends
from infra.postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession


class ApplicationsService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


    async def create_applications(self):
        ...
    

    async def get_applications(self):
        ...


def get_applications_service(
    db_session: AsyncSession = Depends(get_session),
):
    return ApplicationsService(db_session=db_session)
