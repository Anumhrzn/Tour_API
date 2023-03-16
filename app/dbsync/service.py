from pony.orm import db_session
from fastapi import HTTPException
from app.dbsync.sql import SQL_ADD_PLACE, SQL_ADD_USER, SQL_GET_PLACE_BY_NAME, SQL_ADD_USER_RATINGS, \
    SQL_GET_USER_BY_NAME
from app.schemas import UserCreate, PlaceCreate, Ratings, UserLogin
from app.db import db
from pony.orm.dbapiprovider import IntegrityError


class UserService:
    @db_session
    def create_user(self, user_ob: UserCreate):
        sql = SQL_ADD_USER.format(
            name=user_ob.name,
            password=user_ob.password
        )
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="User already registered")

    @db_session
    def login_user(self, user_ob: UserLogin):
        sql = SQL_GET_USER_BY_NAME.format(
            name=user_ob.name,
            password=user_ob.password
        )
        cursor = db.execute(sql)
        print(cursor)
        user = None
        for row in cursor.fetchall():
            id, name, password = row
            user = {
                'name': name,
                'password': password,
            }
            print(user)
        if user is None:
            raise HTTPException(
                status_code=404, detail="User not found")
        else:
            if user['password'] != user_ob.password:
                raise HTTPException(
                    status_code=401, detail="Username or password incorrect")
        return user


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
    def get_user_rating(self, rating_ob: Ratings):
        sql = SQL_ADD_USER_RATINGS.format(
            name=rating_ob.name,
            place_name=rating_ob.place_name,
            rating=rating_ob.rating,
            description=rating_ob.description)
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="User already registered")
