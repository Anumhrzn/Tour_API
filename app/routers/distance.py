from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.dtos.distance_dtos import LocationDto
from app.services.distance_service import getDistance

router = APIRouter(prefix="/api/distance",
                   tags=["Distance"])

user_service = service.UserService()


@router.post("/")
def calculate_distance(starting_point: LocationDto, destination_point: LocationDto):
    return getDistance(starting_point,destination_point)
