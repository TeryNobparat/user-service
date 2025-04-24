from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.schema_user import UserSignin

def crud_signin(user_data: UserSignin, db: Session):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    token = create_access_token(str(user.id))  # ใส่ user_id หรือ payload ตามระบบที่ออกแบบ
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(user.id),
        "username": user.username
    }
