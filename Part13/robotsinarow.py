"""
Draws ten robots in a single horizontal row.

The program calculates even spacing to distribute ten robots across the screen width.
Each robot is positioned at the same Y-coordinate with increasing X-coordinates
to create a neat row of robots from left to right.

Coordinates are adjusted based on the robot's width to ensure proper positioning
and avoid clipping at screen edges.
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

width = robot.get_width()
height = robot.get_height()

screen.fill((0,0,0))
x=60
for i in range(1,10+1):
    screen.blit(robot, (x-width+i*50,100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()