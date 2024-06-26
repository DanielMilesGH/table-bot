import pygame
import sys 
from PIL import Image 
import robots
# import src.python.BaseRobot

clock = pygame.time.Clock()
MAX_SIZE = (400,400)
image = Image.open(r"data\\preset-images\\hard_image.jpg")
image.thumbnail(MAX_SIZE)

screen = pygame.display.set_mode(image.size)
bg = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()



run = True
robot = robots.BaseRobot(0,0)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_w] and robot.get_y() >= 2:
        robot.move(0, -2)
    if keys[pygame.K_s] and robot.get_y() <= image.size[1]-robot.size:
        robot.move(0, 2)
    if keys[pygame.K_a] and robot.get_x() >= 2:
        robot.move(-2, 0)
    if keys[pygame.K_d] and robot.get_x() <= image.size[0]-robot.size:
        robot.move(2, 0)
    screen.fill(0)
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (0,0,255), robot.to_pygame_rect())

    pygame.display.flip()
