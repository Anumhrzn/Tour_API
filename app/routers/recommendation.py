from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import UserCreate
import app.services.recommendation_service as recommendation_service

router = APIRouter(prefix="/api/recommendations",
                   tags=["Recommendations"])


@router.get("/{title}")
def get_recommendation(title: str):
    # user_service.create_user(user_ob=user_ob)
    return recommendation_service.get_recommendations(title)


@router.get("/user/{uuid}")
async def get_userID(uuid: int):
    # user_service.create_user(user_ob=user_ob)
    return await recommendation_service.get_userid(uuid)
