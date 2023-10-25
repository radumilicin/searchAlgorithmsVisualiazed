import math
from typing import List
from PointAstar import PointAstar
from Point import Point

class PQueue:
    def __init__(self):
        self.queue: List[PointAstar] = []
                
    def percolateUp(self):
        i = len(self.queue) - 1
                
        while i != 0 and self.queue[i].combinedCost < self.queue[self.parent(i)].combinedCost:
            self.queue[i], self.queue[self.parent(i)] = self.queue[self.parent(i)], self.queue[i]
            i = self.parent(i)
                        
    def push(self, item: PointAstar):
        if not isinstance(item, PointAstar):
            raise ValueError("Expected an instance of PointAstar")
        self.queue.append(item)
        self.percolateUp()
                
    def parent(self, i):
        return (i - 1) // 2 if i != 0 else 0
                
    def leftChild(self, i):
        return 2 * i + 1
        
    def rightChild(self, i):
        return 2 * i + 2

    def empty(self):
            return len(self.queue) == 0
        
    def percolateDown(self):
        i = 0
        while ((self.leftChild(i) < len(self.queue) and 
                self.queue[self.leftChild(i)].combinedCost < self.queue[i].combinedCost) or 
                (self.rightChild(i) < len(self.queue) and 
                self.queue[self.rightChild(i)].combinedCost < self.queue[i].combinedCost)):
                
                left = self.leftChild(i)
                right = self.rightChild(i)
                if ((left < len(self.queue) and self.queue[left].combinedCost < self.queue[i].combinedCost) and 
                        (right < len(self.queue) and self.queue[right].combinedCost < self.queue[i].combinedCost)):
                    
                        if(self.queue[left].combinedCost <= self.queue[right].combinedCost):
                                self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                                i = left
                        else:
                                self.queue[i], self.queue[right] = self.queue[right], self.queue[i]
                                i = right
                
                else:
                        if ((left < len(self.queue) and self.queue[left].combinedCost < self.queue[i].combinedCost)):
                                self.queue[i], self.queue[left] = self.queue[left], self.queue[i]
                                i = left
                                
                        else:
                                self.queue[i], self.queue[right] = self.queue[right], self.queue[i]
                                i = right

    def dequeue(self):
        first = self.queue[0]
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.queue.pop(-1)
        self.percolateDown()
        return first

                
                
                
                
                        
                
                        

        
                
        


        
                
        
                
        