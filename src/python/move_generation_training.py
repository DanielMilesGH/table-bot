"""

This file is for local testing, it will mimic an API pull to get move generation, and then display
that movement locally with pygame

"""

import pygame
import sys 
from PIL import Image 
# import robots
# import src.python.robots
from imports import nnet
from imports.robots import NeuralRobot
import numpy as np
import random
import copy

NUM_BOTS = 5000
START_POS = (30,15)


MAX_SIZE = (400,400)
image = Image.open(r"data\\preset-images\\hard_image.jpg")
image.thumbnail(MAX_SIZE)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(image.size)
bg = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()


obs = [
    [(0,0),(0,image.size[1])],
    [(0,image.size[1]-1),(image.size[0]-1,image.size[1]-1)],
    [(image.size[0]-1,image.size[1]-1),(image.size[0]-1,0)],
    [(image.size[0]-1,0),(0,0)],

((0, 50), (70, 50)),
((140,0),(140,110)),
((140,110),(50,110))
]

robots = [NeuralRobot(*START_POS) for _ in range(NUM_BOTS)]

run = True
while run:
    frames = 0
    generation = True
    while generation:
        num_alive = 0
        frames+=1
        if not run:
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left click ends current generation
                if event.button == 1:
                    generation = False 
                    continue

        screen.fill(0)
        screen.blit(bg, (0,0))
        clock.tick(60)

        for rob in robots:
            if not rob.alive:
                continue
            rob.nnet_move(obs, rob.size*1, screen)
            if len(rob.total_coords)<7 and frames>10:
                rob.alive = False
                continue
            elif len(rob.total_coords)<20 and frames>30:
                rob.alive=False
                continue

            pygame.draw.rect(screen, (0,0,255), rob.to_pygame_rect())
            num_alive += 1
            
        for ob in obs:
            pygame.draw.line(screen, (0,255,0), ob[0], ob[1], 2)

        pygame.display.flip()

        if (frames > 3333333333) or (num_alive == 0):
            generation=False # early stopping
    # START end of generation logic
    # wont use breeding, just mixing for now 
    best_nnet = None 
    best_fitness = 0 
    for rob in robots:
        rob.alive=True 
        if rob.get_fitness()>best_fitness:
            best_fitness = rob.get_fitness()
            best_nnet = copy.deepcopy(rob.nnet)
    # best nnet is found, now apply that to every robot
    for rob in robots:
        rob.nnet = copy.deepcopy(best_nnet)
        rob.nnet.modify_weights()
        # reset the position
        rob.update_pos(START_POS)
    
    print(f"Best Fitness: {best_fitness}")
    print(f"Network:")
    print(best_nnet.extract_weights())