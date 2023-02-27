from pony.orm import db_session
from fastapi import HTTPException
from app.dbsync.sql import SQL_ADD_PLACE, SQL_ADD_USER, SQL_GET_PLACE_BY_NAME, SQL_ADD_USER_RATINGS
from app.schemas import UserCreate, PlaceCreate, Ratings
from app.db import db
from pony.orm.dbapiprovider import IntegrityError


class UserService:
    @db_session
    def create_user(self, user_ob: UserCreate):
        sql = SQL_ADD_USER.format(
            name=user_ob.name
        )
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="User already registered")


class PlaceService:
    @db_session
    def create_place(self, place_ob: PlaceCreate):
        sql = SQL_ADD_PLACE.format(
            name=place_ob.name,
            image=place_ob.image,
            description=place_ob.description
        )
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="Place already exists")

    @db_session
    def get_place_by_name(self, name):
        sql = SQL_GET_PLACE_BY_NAME.format(name=name)
        cursor = db.execute(sql)
        place = {}
        for row in cursor.fetchall():
            id, name, image, description = row
            place = {
                'name': name,
                'image': image,
                'description': description,
            }
        return place
    

class RatingService:
    @db_session
    def get_user_rating(self,place_ob: Ratings ,rating_ob : Ratings):
        sql = SQL_ADD_USER_RATINGS.format(
            place = place_ob.place,
            rating = rating_ob.rating            )
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="User already registered")        
