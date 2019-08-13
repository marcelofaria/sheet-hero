import pygame
from win32api import GetSystemMetrics

#(width, height) = (int(GetSystemMetrics(0)), int(GetSystemMetrics(1)))
(width, height) = (400,400)
screen = pygame.display.set_mode((width, height))

while True:
    pygame.event.get()
    screen.fill((255,255,255))
    #pygame.display.update()
    pygame.draw.line(screen,(0,0,0), (20,20), (380,20), 2)
    pygame.draw.line(screen,(0,0,0), (20,35), (380,35), 2)
    pygame.draw.line(screen,(0,0,0), (20,50), (380,50), 2)
    pygame.draw.line(screen,(0,0,0), (20,65), (380,65), 2)
    pygame.draw.line(screen,(0,0,0), (20,80), (380,80), 2)
    pygame.display.flip()

#input = input("prompt")
