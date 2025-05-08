from pydantic import BaseModel, EmailStr, constr, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    username: str
    full_name: str
    table_tel: str
    fast_tel: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_active: bool = True

class UserRead(UserBase):
    id: UUID
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True  # สำหรับ SQLAlchemy >= 2.0

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    table_tel: Optional[str] = None
    fast_tel: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True

class UserChangePassword(BaseModel):
    old_password: constr(min_length=6) # type: ignore
    new_password: constr(min_length=6) # type: ignore

    class Config:
        from_attributes = True


class UserSignin(BaseModel):
    username: str = Field(...,min_length=6)
    password: str = Field(...,min_length=8)
