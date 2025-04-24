from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    table_tel = Column(String, unique=True, nullable=False)
    fast_tel = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(String, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
