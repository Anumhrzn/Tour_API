from pydantic import BaseModel


class LocationDto(BaseModel):
    latitude: float
    longitude: float
