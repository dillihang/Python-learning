"""
A simple Pygame animation where a robot sprite moves vertically 
(up and down) in an endless loop. 

The robot image flips vertically each time it changes direction:
- When moving downward, the normal (unflipped) image is used.
- When moving upward, the image is vertically flipped.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 60 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
clock = pygame.time.Clock()

height = robot.get_height()
normal_robot = robot
flipped_robot = pygame.transform.flip(robot, False, True)

current_robot = normal_robot
direction=1
x=0
y=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
        
    if y>=480-height:
        direction=-1
        current_robot=flipped_robot
    if y<=0:
        direction=1
        current_robot= normal_robot

    y+=direction

    window.blit(current_robot, (x, y))
    pygame.display.flip()   
    clock.tick(60)