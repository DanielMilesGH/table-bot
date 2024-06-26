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

def record_line(screen):
    """
    Records a line drawn with two mouse clicks and prints the coordinates.
    """

    drawing = False  # Flag to track drawing state
    start_pos = None
    end_pos = None
    line_color = (0, 255, 0)  # Green line color
    lines = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit if the user quits
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not drawing:  
                    drawing = True
                    start_pos = event.pos  # Record starting point
                else:
                    drawing = False
                    end_pos = event.pos  # Record ending point

                    # Print coordinates for Pygame (tuples)
                    print(f"Line: {start_pos}, {end_pos}")  
                    lines.append((screen, line_color, start_pos, end_pos, 2))
                    # Draw the line on the screen   
        for l in lines:
            pygame.draw.line(*l)

        # Update the display to show the line
        pygame.display.flip()

run = True
robot = robots.BaseRobot(0,0)
pygame.display.set_caption("Moving")
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
    if keys[pygame.K_SPACE]:
        pygame.display.set_caption("Drawing Lines")
        record_line(screen)
        pygame.display.set_caption("Moving")
    screen.fill(0)
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (0,0,255), robot.to_pygame_rect())

    pygame.display.flip()
