import orjson
from fastapi import Depends
from infra.kafka.kafka import KafkaManager, get_kafka_service
from infra.postgres.postgres import get_session
from models.entities import Application
from schemas.app_schemas import (ApplicationCreate, ApplicationKafkaModel,
                                 ApplicationsCreateResponse, ApplicationsInDB,
                                 PaginationSchema)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ApplicationsService:
    def __init__(self, db_session: AsyncSession, kafka_manager: KafkaManager):
        self.db_session = db_session
        self.kafka_service = kafka_manager

    async def create_application(self, application_create: ApplicationCreate) -> ApplicationsCreateResponse:
        application = Application(**application_create.model_dump())

        self.db_session.add(application)
        await self.db_session.commit()
        await self.db_session.refresh(application)

        await self._publish_to_kafka(application)

        return ApplicationsCreateResponse.model_validate(application)

    async def _publish_to_kafka(self, application: Application):
        """Защищенный метод для отправки данных приложения в Kafka."""
        kafka_data = ApplicationKafkaModel(
            id=str(application.id),
            user_name=application.user_name,
            description=application.description,
            created_at=application.created_at,
        )

        await self.kafka_service.send_message(
            'application-topic',
            orjson.dumps(kafka_data.dict()).decode('utf-8')
        )

    async def get_applications(self, pagination: PaginationSchema) -> list[ApplicationsInDB]:
        query = select(Application)

        if pagination.user_name:
            query = query.where(Application.user_name.ilike(f"%{pagination.user_name}%"))

        query = query.offset((pagination.page - 1) * pagination.size).limit(pagination.size)

        result = await self.db_session.execute(query)
        applications = result.scalars().all()

        return [ApplicationsInDB.model_validate(app) for app in applications]



def get_applications_service(
        db_session: AsyncSession = Depends(get_session),
        kafka_service: KafkaManager = Depends(get_kafka_service)

):
    return ApplicationsService(db_session, kafka_service)
