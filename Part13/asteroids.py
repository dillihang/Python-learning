"""
Asteroid Collector Game
-----------------------

A simple arcade-style game built with Pygame.

Description:
    The player controls a robot that moves left and right to catch falling asteroids.
    Each asteroid caught awards 1 point. Missing an asteroid reduces the player's lives.
    The game ends when all lives are lost, displaying a Game Over screen and the final score.

Features:
    - Multiple falling asteroids with random spawn positions.
    - Real-time score tracking and on-screen display.
    - Life counter with a Game Over sequence when lives reach zero.
    - Smooth movement controls (A and D keys).
    - Clear text indicators for points and remaining lives.

Controls:
    - A: Move left
    - D: Move right
    - Close window to quit the game.

Author:
    Dilli
"""
import pygame
import random

current_score = 0
dead_counter = 3

pygame.init()
display = pygame.display.set_mode((640, 480))
robot = pygame.image.load("Part13/robot.png")
rock = pygame.image.load("Part13/small_rock.png")
clock = pygame.time.Clock()

robot_width = robot.get_width()
robot_height = robot.get_height()
rock_width = rock.get_width()
rock_height = rock.get_height()

to_right = False
to_left = False

robot_x = 0
robot_y = 480 - robot_height

random_x = [random.randint(5, 630) for _ in range(6)]
random_y = [random.randint(-480, -50) for _ in range(6)]

def game_mech():

    global current_score
    global dead_counter

    if dead_counter == 0:
        return

    for i in range(6):
        display.blit(rock, (random_x[i], random_y[i]))
        random_y[i] +=1
        if random_y[i] >= 480-rock_height:
            dead_counter -=1
            random_x[i] = random.randint(5, 630)
            random_y[i] = random.randint(-480, -50)

        elif robot_x < random_x[i] + rock_width and robot_x + robot_width > random_x[i] and robot_y < random_y[i] + rock_height and robot_y + robot_height > random_y[i]:
            current_score+=1
            random_x[i] = random.randint(5, 630)
            random_y[i] = random.randint(-480, -50)
    
 

while True:
    pygame.display.set_caption(f"Asteroids")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                to_right = True
            if event.key == pygame.K_a:
                to_left = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                to_right = False
            if event.key == pygame.K_a:
                to_left = False


    display.fill((0, 0, 0))

    game_font = pygame.font.SysFont("Arial", 24)
    Point_text = game_font.render(f"Points: {current_score}", True, (255, 0, 0))
    display.blit(Point_text, (520, 10))
    game_font = pygame.font.SysFont("Arial", 24)
    lives_text = game_font.render(f"Lives left: {dead_counter}", True, (255, 0, 0))
    display.blit(lives_text, (20, 10))

    game_mech()
    display.blit(robot, (robot_x, robot_y))

    if dead_counter == 0:
        final_score = current_score

        display.fill((0, 0, 0))
        game_font = pygame.font.SysFont("Arial", 100)
        end_text = game_font.render(f"GAME OVER", True, (255, 0, 0))

        game_font = pygame.font.SysFont("Arial", 50)
        highestscore_text = game_font.render(f"Your Score: {final_score}", True, (255, 0, 0))

        end_text_w = end_text.get_width()
        end_text_h = end_text.get_height()

        display.blit(end_text, (320-end_text_w//2, 240-end_text_h//2))
        display.blit(highestscore_text, (320 - highestscore_text.get_height()//2, 300 - highestscore_text.get_height()//2))

    if to_right and robot_x<=640-robot_width:
        robot_x+=3
    if to_left and robot_x>=0:
        robot_x-=3

    
    pygame.display.flip()
    clock.tick(60)