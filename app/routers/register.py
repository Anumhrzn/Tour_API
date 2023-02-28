from fastapi import APIRouter, HTTPException
from app.models import User, UserCreate
from app.db import database

router = APIRouter(prefix="/api/register", tags=["Register"])


@router.post("/", response_model=User)
async def create_user(user_data: UserCreate):
    async with database.transaction():
        # Check if user with the same email already exists
        query = User.select().where(User.email == user_data.email)
        existing_user = await database.fetch_one(query)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Create a new user
        # @router.post('/UserCreate')
        query = User.insert().values(**user_data.dict())
        user_id = await database.execute(query)
        return await User.get(user_id)
