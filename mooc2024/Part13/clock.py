"""
Exercise: Analog Clock Display with Pygame

This program displays an analog clock using Pygame which shows the current system time.
The clock face includes:

- A large red outer circle representing the clock boundary.
- A black inner circle to create a border effect.
- A red center circle representing the pivot point.
- Hour, minute, and second hands drawn as lines in blue.
- The window title also displays the current time in "HH:MM:SS" format.

Behavior:
- The hour, minute, and second hands are updated in real-time according to the system clock.
- The hands rotate correctly:
    - Seconds: full rotation in 60 seconds.
    - Minutes: full rotation in 60 minutes.
    - Hours: full rotation in 12 hours.
- The center of the clock is at the center of the window (320, 240 for a 640x480 window).
- The lengths of the hands differ: hour < minute < second for clarity.

Controls:
- Close the window to exit the program.

Requirements:
- Pygame library installed.
- Python datetime module available.

Window size: 640x480 pixels
Frame rate: 60 FPS
"""
import pygame
import math
import datetime

pygame.init()
display = pygame.display.set_mode((640, 480))

center_x = 640/2
center_y = 480/2

clock = pygame.time.Clock()

while True:
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour

    seconds_angle = math.radians(seconds * 6 - 90)
    minutes_angle = math.radians(minutes * 6 - 90)
    hours_angle = math.radians((hours % 12) * 30 + minutes * 0.5 - 90)

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    pygame.display.set_caption(f"Clock - {current_time}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 200)
    pygame.draw.circle(display, (0, 0, 0), (center_x, center_y), 195)
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 10)
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 10)

    seconds_x = center_x + math.cos(seconds_angle) * 180 
    seconds_y = center_y + math.sin(seconds_angle) * 180

    minutes_x = center_x + math.cos(minutes_angle) * 170
    minutes_y = center_y + math.sin(minutes_angle) * 170

    hours_x = center_x + math.cos(hours_angle) * 150
    hours_y = center_y + math.sin(hours_angle) * 150

    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (seconds_x, seconds_y), 1)
    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (minutes_x, minutes_y), 3)
    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (hours_x, hours_y), 5)

    pygame.display.flip()
    clock.tick(60)