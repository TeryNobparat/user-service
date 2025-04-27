from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.crud.crud_permission import crud_create_permission
from app.schemas.schema_permission import PermissionCreate,PermissionRead
from app.models.user import User
from app.core.security import get_current_user


router = APIRouter()

@router.post("/add-permission", response_model= PermissionRead)
def api_create_permission(permission_data:PermissionCreate,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
        return crud_create_permission(permission_data,db)