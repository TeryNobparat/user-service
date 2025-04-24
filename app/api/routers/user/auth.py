from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schema_user import UserSignin
from app.crud.crud_auth import crud_signin

router = APIRouter()

@router.post("/Signin")
def api_authentication(user_data: UserSignin,db: Session = Depends(get_db)):
    return crud_signin(user_data,db)