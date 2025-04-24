from pydantic import BaseModel
from uuid import UUID

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: UUID

    class Config:
        from_attributes = True
