import json

from fastapi_cache.backends.redis import RedisCacheBackend

import app.lib.convertJSON as cj
import heapq as heap
import time

from app.redis_cache import get_cache


async def aStar(source, destination):
    open_list = []
    g_values = {}

    path = {}
    closed_list = {}

    sourceID = cj.getOSMId(source[0], source[1])
    destID = cj.getOSMId(destination[0], destination[1])

    g_values[sourceID] = 0
    h_source = cj.calculateHeuristic(source, destination)

    open_list.append((h_source, sourceID))
    print(open_list)
    s = time.time()
    while (len(open_list) > 0):
        curr_state = open_list[0][1]

        # print(curr_state)
        heap.heappop(open_list)
        closed_list[curr_state] = ""

        if (curr_state == destID):
            print("We have reached to the goal")
            break

        cache: RedisCacheBackend = get_cache()
        cache_key = f'{curr_state}{destination[0]}{destination[1]}'
        print((cache_key))
        in_cache = await cache.get(cache_key)
        if in_cache:
            nbrs = json.loads(in_cache)
        else:
            nbrs = cj.getNeighbours(curr_state, destination)
            await cache.set(cache_key, json.dumps(nbrs))
        print(nbrs)
        values = nbrs[curr_state]
        for eachNeighbour in values:
            neighbourId, neighbourHeuristic, neighbourCost, neighbourLatLon = cj.getNeighbourInfo(
                eachNeighbour)
            current_inherited_cost = g_values[curr_state] + neighbourCost

            if (neighbourId in closed_list):
                continue
            else:
                g_values[neighbourId] = current_inherited_cost
                neighbourFvalue = neighbourHeuristic + current_inherited_cost

                open_list.append((neighbourFvalue, neighbourId))

            path[str(neighbourLatLon)] = {"parent": str(
                cj.getLatLon(curr_state)), "cost": neighbourCost}

        open_list = list(set(open_list))
        heap.heapify(open_list)

    print("Time taken to find path(in second): " + str(time.time() - s))
    return path
