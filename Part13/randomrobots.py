"""
Draws one thousand robots at random positions on the screen.

The program generates random X and Y coordinates within the screen boundaries
for each robot, ensuring all robots remain fully visible on screen.

Random coordinates are calculated considering the robot's dimensions to prevent
any part of the robots from being drawn outside the visible screen area.
The result is a scattered arrangement of robots filling the screen randomly.
"""
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

width = robot.get_width()
height = robot.get_height()

screen.fill((0,0,0))
for i in range(1,1000+1):
    screen.blit(robot, (random.choice(range(1,640))-width, random.choice(range(1,480))))
 
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()