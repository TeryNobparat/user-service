from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid

class RolePermission(Base):
    __tablename__ = "role_permissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(UUID(as_uuid=True), nullable=False)
    permission_id = Column(UUID(as_uuid=True), nullable=False)
