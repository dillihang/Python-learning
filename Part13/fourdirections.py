"""
Exercise Template: Arrow-key controlled robot movement in Pygame.

This program was provided as an exercise template. The task was to 
implement movement so that the player can move a robot sprite in four 
directions using the arrow keys on the keyboard.

Your contribution:
- Implemented movement logic for all four directions:
    - Left arrow: moves the robot left
    - Right arrow: moves the robot right
    - Up arrow: moves the robot up
    - Down arrow: moves the robot down

Behavior:
- Robot moves smoothly while the arrow keys are held down.
- No boundary checks are implemented in this version, so the robot 
  can move outside the window edges.
- Handles KEYDOWN and KEYUP events to track active movement directions.

Controls:
- Use arrow keys to move the robot.
- Close the window to exit.

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

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y +=2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)