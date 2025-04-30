from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session
from app.schemas.schema_role import RoleCreate, RoleRead,RoleUserCreate,RoleUserRead
from app.crud.crud_roles import crud_create_role,crud_add_roles
from app.core.database import get_db
from app.core.security import require_any_permission
from app.models.user import User

router = APIRouter()

@router.post("/add-roles" ,response_model= RoleRead)
def api_create_role(role_data:RoleCreate,db: Session = Depends(get_db), current_user: User = Depends(require_any_permission("MANAGE_PERMISSIONS"))):
    return crud_create_role(role_data,db)


@router.post("/assignment" , response_model=RoleUserRead)
def api_assignment_role(data:RoleUserCreate, db: Session = Depends(get_db), current_user: User = Depends(require_any_permission("MANAGE_PERMISSIONS"))):
    return crud_add_roles(data,db)