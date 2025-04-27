from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.schema_user import UserSignin
from app.core.config import settings


oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def crud_signin(user_data: UserSignin, db: Session):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    token = create_access_token(data={"sub": str(user.id)})
    return {
        "access_token": token,
        "token_type": "bearer",
        "username": user.username,
        "name": user.full_name
    }
