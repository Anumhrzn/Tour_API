from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    # class Config:
    #     orm_mode=True


class PlaceCreate(BaseModel):
    name: str
    image: str
    description: Optional[str]


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    pass

class Ratings(BaseModel):
    place: str
    description:Optional[str]
    rating: float
 