import math
from Point import Point

class PointAstar:
    def __init__(self, point: Point, costToDest: float):
        self.point = point
        self.costToPoint = math.inf
        self.heuristicPointToDest = costToDest
        self.combinedCost = math.inf
                
    def __str__(self):
        return ("Point: " + str(self.point) + 
                " with costToPoint: " + str(self.costToPoint) + 
                " and heuristicPointToDest: " + str(self.heuristicPointToDest) + 
                " and combinedCost: " + str(self.combinedCost) + "\n ")