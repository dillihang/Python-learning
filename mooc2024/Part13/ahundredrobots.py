"""
Draws one hundred robots arranged in a 10x10 grid pattern.

The program uses a single loop with modulo arithmetic to create a grid of 
10 rows with 10 robots in each row. The positioning logic ensures even 
spacing both horizontally and vertically while maintaining consistent 
margins around the grid.

Positioning Algorithm:
- Uses a counter variable `t` to track horizontal position within each row
- When `i % 10 == 1` (at indices 1, 11, 21, etc.), moves to next row by:
  - Resetting horizontal counter `t` to 0
  - Incrementing base X position by 10 pixels for rightward shift
  - Incrementing base Y position by 10 pixels for downward shift
- Calculates X coordinate: starting_pos_x - width + t * 50
- Calculates Y coordinate: starting_pos_y (constant per row)

Parameters:
- Grid: 10 rows × 10 columns (100 total robots)
- Horizontal spacing: 50 pixels between robot centers
- Vertical spacing: 10 pixels between rows  
- Initial position: (60, 100) for first robot
- Each subsequent row shifted 10 pixels right and 10 pixels down

The result is a diagonal grid pattern where each row is offset from the
previous one, creating a stepped arrangement across the screen.
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

width = robot.get_width()
height = robot.get_height()

screen.fill((0,0,0))
starting_pos_x=60
starting_pos_y=100
t=1
for i in range(1,100+1):
    if i%10==1:
        t=0
        starting_pos_x=starting_pos_x+10
        starting_pos_y=starting_pos_y+10
    screen.blit(robot, (starting_pos_x-width+t*50,starting_pos_y))
    t+=1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()