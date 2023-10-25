import pygame
from pygame.locals import *
import random
import math
import numpy as np
import time
from utilities import dist_pythagoras, drawObstacles, initializePointDistances
from Point import Point
from PointAstar import PointAstar
from typing import List
from priorityQueue import PQueue


WINDOW_WIDTH = 600
WINDOW_HEIGHT= 600
SCREEN = (600,600)      # width , height 
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("My Pygame Window")

#   x = (0,20)
#           = 12
#

start_rough = Point(random.randint(0, WINDOW_WIDTH - 1), random.randint(0, WINDOW_WIDTH - 1))
end_rough = Point(random.randint(0, WINDOW_WIDTH - 1), random.randint(0, WINDOW_WIDTH - 1))

BLOCKSIZE = int(20) # Set the size of the grid block

NO_BLOCKS = SCREEN[0] // BLOCKSIZE   # get the number of blocks per axis

start = Point(start_rough.x - start_rough.x % BLOCKSIZE, start_rough.y - start_rough.y % BLOCKSIZE)
end = Point(end_rough.x - end_rough.x % BLOCKSIZE, end_rough.y - end_rough.y % BLOCKSIZE)


def neighbours (point, vis) -> list[(int, int)]:
   pos_neighb = []
   
   for dx in (-1,0,1):
      for dy in (-1,0,1):
            if dx == 0 and dy == 0:
               continue  # Skip the center point
            nx, ny = point.x + dx, point.y + dy
            if 0 <= nx < NO_BLOCKS and 0 <= ny < NO_BLOCKS and not vis[nx][ny] and (abs(point.x - nx) + abs(point.y - ny) != 2):
               pos_neighb.append((nx, ny))
   
   # print("Neighbours :" + str(pos_neighb))
   return pos_neighb


def bfs(start_pos, end_pos, obstacles):
   # st = []
   queue = []
  
   queue.append(start_pos)
   vis = np.full((NO_BLOCKS, NO_BLOCKS), False)                                          # initialize visited array
   parent = np.zeros((NO_BLOCKS, NO_BLOCKS), dtype=Point)                                # initialize parent array
   
   print('Init x = ' + str(start_pos.x) + ' y = ' + str(start_pos.x))
   print('End x = ' + str(end_pos.x) + ' y = ' + str(end_pos.y))
   
   while len(queue) != 0 :                                                                         # until queue is not empty
      pygame.event.pump()
      top = queue[0]
      # print('x = ' + str(top.x) + ' y = ' + str(top.y))
      vis[top.x][top.y] = True
      if(top != start_pos):
         pygame.draw.rect(screen, YELLOW, (top.x * BLOCKSIZE, top.y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
         pygame.display.flip()
         pygame.time.delay(400)

      if(top == end_pos):
         # print("You have reached the end")
         return
      for (x,y) in neighbours(top, vis):
         # print('neighbour x = ' + str(x) + ' y = ' + str(y) + ' and is an obstacle = ' + str(obstacles[x][y])) 
         if not obstacles[x][y] and not vis[x][y]:
            parent[x][y] = Point(top.x, top.y)
            queue.append(Point(x,y))
      queue.pop(0)
   print("It is impossible to reach the end")


def dfs(start_pos, end_pos, obstacles):
   st = []
  
   st.append(start_pos)
   vis = np.full((NO_BLOCKS, NO_BLOCKS), False)
   parent = np.zeros((NO_BLOCKS, NO_BLOCKS), dtype=Point)
   
   print('Init x = ' + str(start_pos.x) + ' y = ' + str(start_pos.y))
   print('End x = ' + str(end_pos.x) + ' y = ' + str(end_pos.y))
   
   while len(st) != 0 :
      pygame.event.pump()
      top = st.pop(-1)
      # print('x = ' + str(top.x) + ' y = ' + str(top.x))
      vis[top.x][top.y] = True
      if(top != start_pos):
         pygame.draw.rect(screen, YELLOW, (top.x * BLOCKSIZE, top.y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
         pygame.display.flip()
         pygame.time.delay(400)
         
      if(top == end_pos):
         print("You have reached the end")
         return
      for (x,y) in neighbours(top, vis):
         # print('neighbour x = ' + str(x) + ' y = ' + str(y) + ' and is ' + str(obstacles[x][y]) + ' an obstacle') 
         if not obstacles[x][y] and not vis[x][y]:
            parent[x][y] = Point(top.x, top.y)
            st.append(Point(x,y))
   print("It is impossible to reach the end")
 
def Astar(start_pos : Point, end_pos : Point, points : List[List[PointAstar]], obstacles):
   queue = PQueue()
   
#    queue.put()
   vis = np.full((NO_BLOCKS, NO_BLOCKS), False)
   parent = np.full((NO_BLOCKS, NO_BLOCKS), Point(0,0))
   
   start_point = points[start_pos.x][start_pos.y]
   start_point.costToPoint = 0
   
   queue.push(start_point)
   
   while not queue.empty():
      pygame.event.pump()
      top = queue.dequeue()
      vis[top.point.x][top.point.y] = True   
      
      if(top.point != start_pos):
         pygame.draw.rect(screen, YELLOW, (top.point.x * BLOCKSIZE, top.point.y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
         pygame.display.flip()
         pygame.time.delay(400)
      
      if(top.point == end_pos):
         print("You have reached the end")
         return   
      
      for (x,y) in neighbours(top.point, vis):
         if not vis[x][y] and not obstacles[x][y]:
            points[x][y].costToPoint = top.costToPoint + 1
            points[x][y].combinedCost = points[x][y].costToPoint + points[x][y].heuristicPointToDest
            queue.push(points[x][y])
   print("It is impossible to reach the end")
    

def drawGrid(color):
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            if((start.x != x and start.y != y) or (end.y != x and end.y != y)):
               rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
               pygame.draw.rect(screen, color, rect, 1)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 128, 0)
RED = (255,0,0)

startRect = pygame.Rect(start.x, start.y, BLOCKSIZE, BLOCKSIZE)
endRect = pygame.Rect(end.x, end.y, BLOCKSIZE, BLOCKSIZE)   # first is width and 2nd is height

obstacles = []
matrixPoints : List[List[PointAstar]] = []

running = True
while running:
   # Handle events
   pygame.event.pump()     # pump the events 

   screen.fill(WHITE)  # Clear the screen
   pygame.draw.rect(screen, GREEN, startRect)
   pygame.draw.rect(screen, RED, endRect)
   
   drawGrid(GRAY)
   
   pygame.display.update()
   obstacles = drawObstacles(screen_dims=SCREEN, block_width=BLOCKSIZE, block_height=BLOCKSIZE, surface=screen, start=start, end=end, alpha=0.3)      # draw obstacles with some probability
   pygame.display.update()
   method = input("What search algorithm do you want to use: ")
   
   start_pos = Point(start.x // BLOCKSIZE, start.y // BLOCKSIZE)      # initialize the start pos as index
   end_pos =  Point(end.x // BLOCKSIZE, end.y // BLOCKSIZE)      # initialize the end pos as index    
   
   if method == "DFS":
      dfs(start_pos, end_pos, obstacles)
      
   elif method == "BFS":
      bfs(start_pos, end_pos, obstacles)
      
   elif method == "Astar":
      matrixPoints = initializePointDistances(end_pos, SCREEN[0] // BLOCKSIZE, SCREEN[1] // BLOCKSIZE)
      Astar(start_pos, end_pos, matrixPoints, obstacles)
      
   running = False
