from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.schemas import PlaceCreate, PlaceUpdate

router = APIRouter(prefix="/api/places",
                   tags=["Places"])

place_service = service.PlaceService()


# @router.get('')
# def get_all_candidates():
#     all_candidates = candidate_service.get_all_candidates()
#     response = generate_candidate_response(all_candidates)
#     return response


@router.post("/addPlaces")
def add_places(place_ob: PlaceCreate):
    place_service.create_place(place_ob=place_ob)


@router.get("/{name}")
def get_place_by_name(name: str):
    data = place_service.get_place_by_name(name)
    return data


@router.post("/updatePlace")
def update_places(places: PlaceUpdate):
    for data in places.datas:
        place_service.update_place(data)

# @router.delete("/deleteCandidate/{candidate_id}")
# def delete_candidate(candidate_id: str):
#     candidate_service.delete_candidate(candidate_id=candidate_id)
