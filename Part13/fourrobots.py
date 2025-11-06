import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Part13/robot.png")

width = robot.get_width()
height = robot.get_height()

screen.fill((0,0,0))
screen.blit(robot, (0,0))
screen.blit(robot, (639-width, 0))
screen.blit(robot, (639-width, 479-height))
screen.blit(robot, (0, 479-height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()