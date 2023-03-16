from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    password: str
    # class Config:
    #     orm_mode=True


class PlaceCreate(BaseModel):
    name: str
    image: str
    description: Optional[str]


class UserCreate(UserBase):
    pass


class UserLogin(UserBase):
    pass


class UserRead(UserBase):
    pass


class Ratings(BaseModel):
    name: str
    place_name: str
    rating: float
    description: Optional[str]
