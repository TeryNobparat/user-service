from pydantic import BaseModel
from uuid import UUID

class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class PermissionRead(PermissionBase):
    id: UUID

    class Config:
        orm_mode = True
