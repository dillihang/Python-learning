"""
Exercise: Click-to-move robot in Pygame.

This program displays a robot at a random location within the window.
When the player clicks on the robot, it instantly moves to a new random location.

Behavior:
- Robot spawns initially at a random position fully inside the 640x480 window.
- When the mouse is clicked:
    - The program checks if the click is inside the robot's rectangle.
    - If so, the robot is relocated to a new random position within the window boundaries.
- Robot always stays fully visible on the screen.

Controls:
- Move the mouse and click on the robot to make it jump to a new random location.
- Close the window to exit.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Frame rate: 600 FPS (smooth instant updates for clicks).
"""
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

width = robot.get_width()
height = robot.get_height()

robot_x=random.randint(1,639-width)
robot_y=random.randint(1,480-height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_x, mouse_y = event.pos
          if robot_x <= mouse_x <= robot_x + width and robot_y <= mouse_y <= robot_y + height:
              robot_x = random.randint(1,639-width)
              robot_y = random.randint(1,479-height)

        if event.type == pygame.QUIT:
            exit(0)
    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    
    clock.tick(600)