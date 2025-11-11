"""
A Pygame animation where ten robot sprites move in a circle around the 
center of the window.

- The robots are evenly spaced around the circle.
- All robots rotate together as the main angle increases over time.

Notes:
- This solution heavily relies on the teacher's example for the circular 
  motion formula and guidance.
- Additional help from ChatGPT was used to implement evenly spaced offsets 
  for multiple robots.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 120 FPS
"""
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

angle = 0
i=0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))

    for i in range(10):
        offset = i * (2 * math.pi / 10)
        x = 320+math.cos(angle+offset)*100-robot.get_width()/2
        y = 240+math.sin(angle+offset)*100-robot.get_height()/2

        window.blit(robot, (x, y))
 
    pygame.display.flip()

    angle += 0.01
  
    clock.tick(120)