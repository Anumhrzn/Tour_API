from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import UserCreate
import app.services.recommendation_service as recommendation_service

router = APIRouter(prefix="/api/recommendations",
                   tags=["Recommendations"])

# @router.get('')
# def get_all_candidates():
#     all_candidates = candidate_service.get_all_candidates()
#     response = generate_candidate_response(all_candidates)
#     return response


@router.get("/{title}")
def get_recommendation(title: str):
    # user_service.create_user(user_ob=user_ob)
    return recommendation_service.get_recommendations(title)


@router.get("/user/{uuid}")
async def get_userID(uuid: int):
    # user_service.create_user(user_ob=user_ob)
    return await recommendation_service.get_userid(uuid)


# @router.delete("/deleteCandidate/{candidate_id}")
# def delete_candidate(candidate_id: str):
#     candidate_service.delete_candidate(candidate_id=candidate_id)
