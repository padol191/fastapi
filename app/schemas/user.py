from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    login: Optional[str]
    password_hash:Optional[str]
    email: Optional[EmailStr] = None
    activated: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    login: str
    password_hash: str
    

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# Properties to receive via API on update
class UserUpdate(UserBase):
    password_hash: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


# Additional properties stored in DB but not returned by API
class UserInDB(UserInDBBase):
    hashed_password: Optional[str]