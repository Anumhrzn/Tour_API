from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import UserCreate, UserLogin

router = APIRouter(prefix="/api/users",
                   tags=["Users"])

user_service = service.UserService()


@router.post("/addUser")
def add_user(user_ob: UserCreate):
    user_service.create_user(user_ob=user_ob)


@router.post("/login")
def login_user(user_ob: UserLogin):
    return user_service.login_user(user_ob=user_ob)

