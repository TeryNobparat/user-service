from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.database import get_db
from app.crud.crud_user import crud_user_registor, crud_change_password,crud_edit_user
from app.schemas.schema_user import UserCreate, UserRead, UserChangePassword , UserUpdate

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=201)
def api_register_user(user_create: UserCreate, db: Session = Depends(get_db)):
    return crud_user_registor(user_create, db)

@router.post("/{user_id}/change-password", response_model=UserRead, status_code=200)
def api_change_password(user_id: UUID, password_data: UserChangePassword, db: Session = Depends(get_db)):
    return crud_change_password(user_id, password_data, db)

@router.post("/{user_id}/edit-detail", response_model=UserRead, status_code=200)
def api_edit_user(user_id: UUID, userupdate: UserUpdate, db: Session = Depends(get_db)):
    return crud_edit_user(user_id,userupdate,db)


