"""
Exercise Template: Mouse-following robot in Pygame.

This program was provided as an exercise template. The goal of the exercise
was to make the robot follow the mouse cursor so that its centre always aligns
with the current mouse position.

Your implementation:
- Captures MOUSEMOTION events to track the mouse's position in real time.
- Updates the robot's position so that its centre (not top-left corner) 
  matches the cursor.
- Ensures smooth, instant movement following the mouse.

Behavior:
- When the mouse moves, the robot immediately follows and stays centred 
  on the cursor.
- The robot updates position every frame based on mouse coordinates.
- The display refreshes at 600 FPS for smooth visual tracking.

Controls:
- Move the mouse to move the robot.
- Close the window to exit.

Requirements:
- Pygame library installed.
- 'robot.png' image located in the 'Part13/' directory.

Frame rate: 600 FPS
"""
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    
    robot_x = target_x
    robot_y = target_y
    

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(600)