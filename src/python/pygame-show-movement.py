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

clock = pygame.time.Clock()
MAX_SIZE = (400,400)
image = Image.open(r"data\\preset-images\\hard_image.jpg")
image.thumbnail(MAX_SIZE)

screen = pygame.display.set_mode(image.size)
bg = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()

# Make the lines list a global variable, so the lines stay after reverting back to movement
lines = []

def record_line(screen):
    """
    Records a line drawn with two mouse clicks and prints the coordinates.
    """
    drawing = False  # Flag to track drawing state
    start_pos = None
    end_pos = None
    line_color = (0, 255, 0)  # Green line color

    recording = True
    while recording:
        pygame.display.set_caption(f"Drawing - Start:{start_pos} End:{end_pos}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit if the user quits

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                recording = False  # Stop recording and switch to movement when ESC is pressed

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left click for drawing
                if event.button == 1:
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
                        # start_pos = None # Reset starting position after drawing line

                # Right click for undo
                if event.button == 3:
                    start_pos=None
                    end_pos=None
                    drawing = False

        if drawing and start_pos:
            end_pos = pygame.mouse.get_pos() # Update the end position to follow the cursor

        # Ensures that the line doesn't color the screen        
        screen.fill(0)
        screen.blit(bg, (0, 0))

        for l in lines:
            if robot.check_collision(l):
                l = (l[0], (255, 0, 0), l[2], l[3], l[4])  # Change color to red
            pygame.draw.line(*l)


        if drawing and start_pos and end_pos:
            pygame.draw.line(screen, line_color, start_pos, end_pos, 2)

        # Keeps the square on the screen while drawing the line    
        pygame.draw.rect(screen, (0, 0, 255), robot.to_pygame_rect())        
        # Update the display to show the line
        pygame.display.flip()


def lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
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


run = True
robot = robots.PygameRobot(0,0)
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

    # Adding this makes the lines stay when switching between recording and movement
    for l in lines:
        if robot.check_collision(l):
            l = (l[0], (255, 0, 0), l[2], l[3], l[4])  # Change color to red
        pygame.draw.line(*l)

    pygame.draw.rect(screen, (0,0,255), robot.to_pygame_rect())

    pygame.display.flip()
