from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.permission import Permission
from app.schemas.schema_permission import PermissionCreate,PermissionRead

def crud_create_permission(permission_data:PermissionCreate, db: Session = Depends(get_db)):
    permis = db.query(Permission).filter(Permission.name == permission_data.name).first()

    if permis:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="permission already !!")
    
    new_permission = Permission(**permission_data.dict())
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return PermissionRead.from_orm(new_permission)