"""
A Pygame animation where multiple robot sprites fall from above the screen 
and reappear in random horizontal positions when they go off-screen. 

Behavior:
- Each robot starts off-screen with a random vertical (y) and horizontal (x) position.
- Robots move downward at a constant speed.
- When a robot reaches the bottom of the window or drifts too far left/right:
    - Its vertical position is reset above the screen (off-screen).
    - Its horizontal position is assigned a new random value.
- This creates a continuous, dynamic stream of robots appearing from the top.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- 'robot.png' located in the 'Part13/' directory.

Window size: 640x480 pixels
Frame rate: 200 FPS (or as set in clock.tick)
"""
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
clock = pygame.time.Clock()

height = robot.get_height()
normal_robot = robot

end_position = 480-height
mid_position = 640/2
end_x_pos = 650-robot.get_width()
end_x_neg_pos = -10-robot.get_width()
random_x = [random.randint(1,639) for _ in range(7)]
random_y = [random.randint(-480,-1) for _ in range(7)]

def creating_robots():
   for i in range(7):
      window.blit(robot, (random_x[i], random_y[i]))
      random_y[i] +=1
      if random_y[i] >=480-height:
          random_y[i] = end_position
          if random_x[i]>mid_position:
            random_x[i]+=1
          else:
             random_x[i]-=1
          
          if random_x[i]>= end_x_pos or random_x[i] <= end_x_neg_pos:
             random_x[i] = random.randint(0, 640)
             random_y[i] = random.randint(-480, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    creating_robots()
    
    pygame.display.flip()  
    clock.tick(200)