"""
Exercise Template: Arrow-key controlled robot movement in Pygame.

This program was provided as an exercise template. The original version 
allowed the robot to move with arrow keys, but did not fully prevent it 
from passing outside the window boundaries.

Your improvement:
- Modified the program so that the robot **cannot pass outside the window**
  in any of the four directions (top, bottom, left, right).
- Added boundary checks before updating the robot's position.
- Ensured smooth continuous movement while holding arrow keys.

Behavior:
- Arrow keys control the robot's movement:
    - Left arrow: moves left
    - Right arrow: moves right
    - Up arrow: moves up
    - Down arrow: moves down
- Robot is constrained within the 640x480 window.
- Movement continues while the key is held down.

Controls:
- Use arrow keys to move the robot.
- Close the window to exit.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Frame rate: 60 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
x = 0
y = 480-robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x < 640 - robot.get_width():
        x += 2
    if to_left and x > 0:
        x -= 2
    if to_up and y > 0:
        y -= 2
    if to_down and  y < 480-robot.get_height():
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)