from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schema_role import RoleCreate, RoleRead,RoleUserCreate,RoleUserRead
from app.models.role import Role
from app.models.user import User
from app.models.user_role import UserRole
from uuid import UUID


def crud_create_role(role_data: RoleCreate, db: Session) -> RoleRead:
    role = db.query(Role).filter(Role.name == role_data.name).first()
    if role:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Roles already exists")

    new_role = Role(**role_data.dict())
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return RoleRead.from_orm(new_role)



def crud_add_roles(data: RoleUserCreate, db: Session):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID does not exist in server!!"
        )

    role = db.query(Role).filter(Role.id == data.role_id).first()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role does not exist!!"
        )

    user_role = db.query(UserRole).filter(
        UserRole.user_id == data.user_id,
        UserRole.role_id == data.role_id
    ).first()
    if user_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request is duplicate!!"
        )

    new_assignment = UserRole(**data.dict())
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)

    return RoleUserRead.from_orm(new_assignment)




