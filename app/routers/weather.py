from fastapi import APIRouter, HTTPException, Depends
import app.dbsync.service as service
import app.services.weather_service as weather_service

router = APIRouter(prefix="/api/weather",
                   tags=["Weather"])

user_service = service.UserService()


@router.get("/")
def get_weather(location: str):
    return weather_service.get_locations(location)

