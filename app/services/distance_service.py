import app.lib.convertJSON as cj
import app.lib.astar as algo
import json


def getDistance(starting_point, destination_point):
    inputStartLoc = (starting_point.latitude, starting_point.longitude)
    inputDestLoc = (destination_point.latitude, destination_point.longitude)
    mappedSourceLoc = cj.getKNN(inputStartLoc)
    mappedDestLoc = cj.getKNN(inputDestLoc)
    path = algo.aStar(mappedSourceLoc, mappedDestLoc)
    # print(path)
    finalPath, cost = cj.getResponsePathDict(path, mappedSourceLoc, mappedDestLoc)

    print("Cost of the path(km): " + str(cost))
    return {'path': finalPath, 'distance': cost}
