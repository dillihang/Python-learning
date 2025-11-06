"""
A simple Pygame animation where two robot sprites move horizontally 
back and forth across the window at different speeds.

- The upper robot moves left and right at normal speed.
- The lower robot moves left and right at double that speed.

Each robot reverses direction when reaching the left or right edge 
of the window, creating a smooth continuous motion.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 300 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
clock = pygame.time.Clock()

height = robot.get_height()
width = robot.get_width()

robotA=robot
robotB=robot
directionA=1
directionB=1
x1=0
x2=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if x1>=640-width:
        directionA=-1

    if x1<=0:
        directionA=1
                
    x1+=directionA
    
    window.blit(robotA, (x1, 100))

    if x2>=640-width:
        directionB=-1

    if x2<=0:
        directionB=1
                
    x2+=directionB*2
    
    window.blit(robotB, (x2, 200))
    
    pygame.display.flip()   
    clock.tick(300)