import pygame
import sys 
from PIL import Image 
import math
# import robots
# import src.python.robots
from imports import robots

clock = pygame.time.Clock()
MAX_SIZE = (400,400)
image = Image.open(r"data\\preset-images\\easy_image.jpg")
image.thumbnail(MAX_SIZE)

screen = pygame.display.set_mode(image.size)
bg = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()

# Make the lines list a global variable, so the lines stay after reverting back to movement
polys = []



run = True
robot = robots.PygameRobot(0,0)
pygame.display.set_caption("Moving")
points = []
screen.blit(bg, (0,0))
def sort_points(points):
    # Calculate the center of the square
    center_x = sum(p[0] for p in points) / 4
    center_y = sum(p[1] for p in points) / 4

    # Sort points based on the angle from the center
    sorted_points = sorted(points, key=lambda p: math.atan2(p[1] - center_y, p[0] - center_x))

    return sorted_points
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left click for drawing
            if event.button == 1:
                points.append(event.pos)  # Record point 

    if len(points) == 4:
        points = sort_points(points)
        # pygame.draw.polygon(screen, (0,255,0), sort_points(points), 2)
        # above is how it should be drawn, below is what collision checks look like
        pygame.draw.line(screen, (0,255,0), points[0], points[1], 2)
        pygame.draw.line(screen, (0,255,0), points[1], points[2], 2)
        pygame.draw.line(screen, (0,255,0), points[2], points[3], 2)
        pygame.draw.line(screen, (0,255,0), points[3], points[0], 2)

        print(sort_points(points))
        points = []

    pygame.display.flip()