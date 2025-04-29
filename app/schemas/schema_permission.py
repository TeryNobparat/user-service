from pydantic import BaseModel
from uuid import UUID

class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class PermissionRead(PermissionBase):
    id: UUID

    class Config:
        from_attributes = True


     
class RolePermission(BaseModel):
    permission_id : UUID
    role_id : UUID

class RoleRolePermissionCreate(RolePermission):
    pass

class RoleRolePermissionRead(RolePermission):
    id: UUID

    class Config:
        from_attributes = True   
