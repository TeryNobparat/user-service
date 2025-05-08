from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.crud.crud_permission import crud_create_permission,crud_add_permission
from app.schemas.schema_permission import PermissionCreate,PermissionRead,RoleRolePermissionRead,RoleRolePermissionCreate
from app.models.user import User
from app.core.security import require_any_permission


router = APIRouter()

@router.post("/add-permission", response_model= PermissionRead)
def api_create_permission(permission_data:PermissionCreate,db: Session = Depends(get_db), current_user: User = Depends(require_any_permission("MANAGE_PERMISSIONS"))):
        return crud_create_permission(permission_data,db)


@router.post("/assignment", response_model=RoleRolePermissionCreate)
def api_assignments(data:RoleRolePermissionCreate,db: Session = Depends(get_db), current_user: User = Depends(require_any_permission("MANAGE_PERMISSIONS"))):
        return crud_add_permission(data,db)

