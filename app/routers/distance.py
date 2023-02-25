from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
from app.dtos.distance_dtos import LocationDto
from app.services.distance_service import get_distance
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/api/distance",
                   tags=["Distance"])

user_service = service.UserService()


@router.post("/")
async def calculate_distance(starting_point: LocationDto, destination_point: LocationDto):
    json_compatible_starting_point = jsonable_encoder(starting_point)
    json_compatible_destination_point = jsonable_encoder(destination_point)
    return await get_distance(json_compatible_starting_point, json_compatible_destination_point)
