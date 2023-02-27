from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import Ratings

router = APIRouter(prefix="/api/rating",
                   tags=["Ratings"])

rating_service = service.RatingService()


@router.post("/addUserRating")
def add_user_rating(rating_ob: Ratings):
    rating_service.get_user_rating(rating_ob=rating_ob)
