# searchAlgorithmsVisualiazed

This project was built to visualize different graph search algorithms: BFS, DFS & A*.

It was done using PyGame, which is a python library for games with which you can render 
on the screen and handle events.

It was incredibly fun working on this project especially on the A* one as the algorithm is 
actually "intelligent" in a sense. The priority queue was also implemented by me. 

BFS - breadth first search
DFS - depth first search
A* - an algorithm using heuristics

The main idea of A* is that it goes on the most optimal path that it finds at that particular point.
A* is like a BFS but with a priority queue instead of a regular queue. The priority queue is used so that the
minimum element is always at the first position. This is necessary because we want the 
totalCost = costToNode(from start to current node) + distFromNodeToDest (calculated with pythagoras) of a 
node to be minimal when exploring a new node. 

The walls in the maze are generated with a function which based on a probability threshold either puts a wall in the
current position or not. To improve the probability of an actually feasible maze being generated, i.e. walls do not 
separate the start point from the end point, a lower probability threshold is chosen. 

It is clear that BFS and DFS are quire "stupid" algorithms, in the sense that they do not operate with a specific 
strategy in mind. A* is a big improvement as the paths the algorithm takes are almost always the shortest.
