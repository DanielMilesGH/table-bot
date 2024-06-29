import sys
import random
print(sys.path)

import pygame
# import nnet
from imports import nnet
class BaseRobot():
    x: int # positive integer
    y: int # positive integer 
    def __init__(self, x:int, y:int, pos:tuple[int,int] | None = None):
        if (pos != None):
            self.x=pos[0]
            self.y=pos[1]
        else:  
            self.x = x
            self.y = y 
        
        # images should be 400x400, making robot length 0.05 image
        self.size = 20

    def get_pos(self) -> tuple[int,int]:
        return (self.x, self.y)
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y 

    # returns params to make pygame rect
    def get_pos_width(self) -> tuple[int,int,int,int]:
        return (self.x, self.y, self.size, self.size)
    
    def update_pos(self, pos:tuple[int,int]):
        self.x=pos[0]
        self.y=pos[1]

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy
    

class PygameRobot(BaseRobot):
    # inherits all base methods
    def to_pygame_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def lines_intersect(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        Check if two line segments intersect.
        """
        def ccw(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        A = (x1, y1)
        B = (x2, y2)
        C = (x3, y3)
        D = (x4, y4)
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    
    def check_collision(self, line):

        robot_rect = self.to_pygame_rect()
        x1, y1 = line[2]
        x2, y2 = line[3]
        
        # Check for intersection with all four edges of the robot's rectangle
        edges = [
            ((robot_rect.left, robot_rect.top), (robot_rect.right, robot_rect.top)),
            ((robot_rect.right, robot_rect.top), (robot_rect.right, robot_rect.bottom)),
            ((robot_rect.right, robot_rect.bottom), (robot_rect.left, robot_rect.bottom)),
            ((robot_rect.left, robot_rect.bottom), (robot_rect.left, robot_rect.top)),
        ]
        for edge in edges:
            if self.lines_intersect(x1, y1, x2, y2, edge[0][0], edge[0][1], edge[1][0], edge[1][1]):
                return True
        return False

class NeuralRobot(PygameRobot):
    def __init__(self, x:int, y:int, pos:tuple[int,int] | None = None):
        super().__init__(x,y,pos)
        self.nnet = nnet.Nnet(4, 6, 2)
        self.alive = True 
        self.fitness = 0
        self.total_coords = set() 
    
    def get_fitness(self):
        # can be changed later to include time
        return len(self.total_coords)
    
    def get_vision(self, obs, dist, screen=None) -> list[int,int,int,int]:
        # centered about its center, not its actual coords
        # vision is currently binary
        centerX = self.x+(self.size//2)
        centerY = self.y+(self.size//2)
        if (dist < self.size//2):
            raise ValueError("dist should be greater than size//2")
        
        north = ((centerX,centerY), (centerX,centerY-dist))
        south = ((centerX,centerY), (centerX,centerY+dist))
        east =  ((centerX,centerY), (centerX+dist,centerY))
        west =  ((centerX,centerY), (centerX-dist,centerY))

        if screen!=None:
            pygame.draw.line(screen, (255,0,0), north[0], north[1], 2)
            pygame.draw.line(screen, (255,0,0), south[0], south[1], 2)
            pygame.draw.line(screen, (255,0,0), east[0], east[1], 2)
            pygame.draw.line(screen, (255,0,0), west[0], west[1], 2)

        hits = [0,0,0,0]
        # there's gotta be a better way, but this works
        for ob in obs:

            if self.lines_intersect(north[0][0], north[0][1], north[1][0], north[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                hits[0] = 1
                
            if self.lines_intersect(south[0][0], south[0][1], south[1][0], south[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                hits[1] = 1

            if self.lines_intersect(east[0][0], east[0][1], east[1][0], east[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                hits[2] = 1

            if self.lines_intersect(west[0][0], west[0][1], west[1][0], west[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                hits[3] = 1

        # check if alive still
        north = ((centerX,centerY), (centerX,centerY-1))
        south = ((centerX,centerY), (centerX,centerY+1))
        east =  ((centerX,centerY), (centerX+1,centerY))
        west =  ((centerX,centerY), (centerX-1,centerY))

        for ob in obs:
            if self.lines_intersect(north[0][0], north[0][1], north[1][0], north[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                self.alive = False
                
            elif self.lines_intersect(south[0][0], south[0][1], south[1][0], south[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                self.alive = False

            elif self.lines_intersect(east[0][0], east[0][1], east[1][0], east[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                self.alive = False

            elif self.lines_intersect(west[0][0], west[0][1], west[1][0], west[1][1],
                                      ob[0][0], ob[0][1], ob[1][0], ob[1][1]):
                self.alive = False
        return hits

    def nnet_move(self, obs, dist, screen=None):
        dx, dy = 0, 0
        vision = self.get_vision(obs, dist, screen)
        outs = self.nnet.get_outputs(vision)
        if vision == [0,0,0,0]:
            # saw nothing state, we need to do a random move
            # otherwise we get deadlocked
            self.move(random.choice([-1,0,1]),random.choice([-1,0,1]))
            if (self.x,self.y) not in self.total_coords:
                self.total_coords.add((self.x,self.y))

        else:
            # by using 0.5, we force a movement
            if outs[0] > 0.5:
                dx = 1
            elif outs[0] < 0.5:
                dx = -1
            
            if outs[1] > 0.5:
                dy = 1
            elif outs[1] < 0.5:
                dy = -1

            if (self.x,self.y) not in self.total_coords:
                self.total_coords.add((self.x,self.y))

            self.move(dx,dy)
    



if __name__ == "__main__":
    print("This is meant for importing!")
