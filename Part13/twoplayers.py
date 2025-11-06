"""
Exercise Template Extension: Two-player robot control in Pygame.

This program builds upon the previous single-player robot movement exercise. 
Originally, the exercise allowed one robot to move within the window using 
the arrow keys. The task here was to extend the program so that *two players* 
can control their own robots independently.

Your improvement:
- Added a second robot with its own position tracking.
- Assigned separate movement controls for each player:
    - Player 1 uses the arrow keys (← ↑ ↓ →).
    - Player 2 uses the W, A, S, and D keys.
- Added independent movement logic and boundary checks for both robots so 
  neither can leave the 640x480 window area.

Behavior:
- Each player moves their robot smoothly while holding down the corresponding keys.
- Both robots remain fully visible within the screen boundaries at all times.
- The window updates at a consistent frame rate to ensure smooth animation.

Controls:
- Player 1: Arrow keys
- Player 2: W, A, S, D
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

x2 = 0
y2 = 0

to_right = False
to_left = False
to_up = False
to_down = False

x2_right = False
x2_left = False
x2_up = False
x2_down = False



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
            
            if event.key == pygame.K_a:
                x2_left = True
            if event.key == pygame.K_d:
                x2_right = True
            if event.key == pygame.K_w:
                x2_up = True
            if event.key == pygame.K_s:
                x2_down = True
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            
            if event.key == pygame.K_a:
                x2_left = False
            if event.key == pygame.K_d:
                x2_right = False
            if event.key == pygame.K_w:
                x2_up = False
            if event.key == pygame.K_s:
                x2_down = False

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
    
    if x2_right and x2 < 640 - robot.get_width():
        x2 += 2

    if x2_left and x2 > 0:
        x2 -= 2

    if x2_up and y2 > 0:
        y2 -= 2
        
    if x2_down and  y2 < 480-robot.get_height():
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)