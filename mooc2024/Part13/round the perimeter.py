"""
A simple Pygame animation where a robot sprite traces the perimeter 
of the window in a continuous loop.

The robot moves clockwise around the edges:
- Right along the top
- Down along the right edge
- Left along the bottom
- Up along the left edge

Each time the robot changes vertical direction (up or down),
its image is flipped vertically for visual effect.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 120 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
clock = pygame.time.Clock()

height = robot.get_height()
width = robot.get_width()
normal_robot = robot
flipped_robot = pygame.transform.flip(robot, False, True)

current_robot = normal_robot
direction=1
x=0
y=0
right_cord = 640-width

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    if x>=640-width:
        
        x=right_cord
        y+=direction

    if x<=0:
        x=0
        y+=direction
                
    if y>=480-height:
        direction=-1
        current_robot=flipped_robot
    if y<=0:
        direction=1
        current_robot= normal_robot

    x+=direction
    

    window.blit(current_robot, (x, y))
    pygame.display.flip()   
    clock.tick(120)