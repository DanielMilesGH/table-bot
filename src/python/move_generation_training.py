"""

This file is for local testing, it will mimic an API pull to get move generation, and then display
that movement locally with pygame

"""

import pygame
import sys 
from PIL import Image 
# import robots
# import src.python.robots
from imports import robots
import numpy as np
import random
from imports.nnet import Nnet 

clock = pygame.time.Clock()
MAX_SIZE = (400,400)
image = Image.open(r"data\\preset-images\\hard_image.jpg")
image.thumbnail(MAX_SIZE)

screen = pygame.display.set_mode(image.size)
bg = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()


#TODO REPLACE THIS LIST COMPREHENSION WITH API CALL
movements = [(random.choice([-5,0,5]),random.choice([-5,0,5])) for i in range(500)]

run = True
robot = robots.PygameRobot(0,0)
pygame.display.set_caption("Moving")
for mov in movements:
    if not run:
        pygame.quit()
        break
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    robot.move(*mov)
    if robot.get_x() > image.size[0]-robot.size:
        robot.x = 400
    if robot.get_x() < 0:
        robot.x=0
    if robot.get_y() > image.size[1]-robot.size:
        robot.y = 400
    if robot.get_y() < 0:
        robot.y = 0


    screen.fill(0)
    screen.blit(bg, (0,0))

    pygame.draw.rect(screen, (0,0,255), robot.to_pygame_rect())

    pygame.display.flip()
