from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

class PageBase(BaseModel):
    title: str
    path: str
    permission_name: Optional[str] = None
    icon: Optional[str] = None
    parent_id: Optional[UUID] = None
    order_index: Optional[int] = 0
    is_active: Optional[bool] = True

class PageCreate(PageBase):
    pass

class PageRead(PageBase):
    id: UUID
    children: Optional[List["PageRead"]] = []

    class Config:
        orm_mode = True
