from pydantic import BaseModel
from typing import Optional, Any


class UserBase(BaseModel):
    name: str
    password: str
    # class Config:
    #     orm_mode=True


class PlaceCreate(BaseModel):
    name: str
    image: str
    description: Optional[str]
    latitude: float
    longitude: float


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


class PlaceUpdate(BaseModel):
    datas: Any
