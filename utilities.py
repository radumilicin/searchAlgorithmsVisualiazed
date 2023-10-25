import random
import pygame
import numpy as np
from Point import Point
import math
from PointAstar import PointAstar
from typing import List

# multiply the distance by 10 to get more different results
def dist_pythagoras(start : Point, dest : Point):
        return math.sqrt(math.pow(abs(start.x - dest.x), 2) + math.pow(abs(start.y - dest.y), 2)) * 10

BLACK=(255,255,255)
BLUE=(0,0,255)

# draw obstacles with probability alpha such that they do not overlap with either start or end
def drawObstacles (screen_dims, block_width, block_height, surface, start, end, alpha) -> list[(int, int)]:
        prob = 0
        width = screen_dims[0]
        height = screen_dims[1]
        
        NO_BLOCKS = width // block_width
        
        start_idx = Point(start.x // block_width, start.y // block_height)
        end_idx = Point(end.x // block_width, end.y // block_height)
        
        obstacles = np.full((NO_BLOCKS, NO_BLOCKS), False)
        for x in range(NO_BLOCKS):
                for y in range(NO_BLOCKS):
                        block_point = Point(x,y)
                        if(block_point != start_idx and block_point != end_idx):
                                prob = random.randint(0,1000) / 1000
                                if(prob <= alpha):				                                        # if probability is larger than alpha then draw obstacle
                                        rect=(x * block_width, y * block_height, block_width, block_height)
                                        obstacles[x][y] = True
                                        pygame.draw.rect(surface, BLUE, rect)
        pygame.display.flip()
        return obstacles

def initializePointDistances(end: Point, width : int, height : int) -> List[List[PointAstar]]:
        matrixPoints : List[List[PointAstar]] = [[None for _ in range(width)] for _ in range(height)]
        
        for i in range(0, width):
                for j in range(0, height):
                        matrixPoints[i][j] = PointAstar(Point(i,j), dist_pythagoras(Point(i,j), end))
                        
                        
        return matrixPoints 

                        
        
				
		