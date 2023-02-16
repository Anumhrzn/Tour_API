from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import UserCreate

router = APIRouter(prefix="/api/users",
                   tags=["Users"])

user_service = service.UserService()


# @router.get('')
# def get_all_candidates():
#     all_candidates = candidate_service.get_all_candidates()
#     response = generate_candidate_response(all_candidates)
#     return response


@router.post("/addUser")
def add_user(user_ob: UserCreate):
    user_service.create_user(user_ob=user_ob)


# @router.delete("/deleteCandidate/{candidate_id}")
# def delete_candidate(candidate_id: str):
#     candidate_service.delete_candidate(candidate_id=candidate_id)
