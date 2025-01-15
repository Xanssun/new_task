import uuid
from datetime import datetime

from infra.postgres.postgres import Base
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID


class Application(Base):
    __tablename__ = 'application'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    user_name = Column(
        String,
        nullable=False,
    )
    description = Column(
        Text,
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
