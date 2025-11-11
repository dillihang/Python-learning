"""
A Pygame animation where a ball sprite bounces off the edges of the window.

- The ball moves diagonally across the screen using independent horizontal 
  and vertical velocities.
- When the ball hits a window edge, its velocity in that direction is reversed,
  causing a bounce effect.
- The ball starts at the center of the screen with initial velocities of 2 
  pixels per frame in both horizontal and vertical directions.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'ball.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 120 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
ball = pygame.image.load("Part13/ball.png")
clock = pygame.time.Clock()

width = ball.get_width()
height = ball.get_height()

horizontally=2
vertically=2
x = 320
y = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))

    if x<=0 or x>=640-width:
        horizontally=-horizontally

    if y<=0 or y>=480-height:
        vertically=-vertically

    x = x + horizontally
    y = y + vertically

    pygame.display.flip()

    clock.tick(120)