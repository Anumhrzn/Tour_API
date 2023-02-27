import app.lib.convertJSON as cj
import app.lib.astar as algo
from app.redis_cache import get_cache
from app.redis_cache.decorators import cache
from fastapi_cache.backends.redis import RedisCacheBackend

import json


@cache()
async def get_distance(starting_point, destination_point):
    inputStartLoc = (starting_point['latitude'], starting_point['longitude'])
    inputDestLoc = (destination_point['latitude'], destination_point['longitude'])
    mappedSourceLoc = cj.getKNN(inputStartLoc)
    mappedDestLoc = cj.getKNN(inputDestLoc)
    path = await algo.aStar(mappedSourceLoc, mappedDestLoc)
    # print(path)
    finalPath, cost = cj.getResponsePathDict(path, mappedSourceLoc, mappedDestLoc)

    print("Cost of the path(km): " + str(cost))
    return {'path': finalPath, 'distance': cost}
