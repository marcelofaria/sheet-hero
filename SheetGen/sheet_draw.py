import pygame as pyg
import os
from win32api import GetSystemMetrics


def draw_note(note, x, y):
    note_figure = pyg.image.load(os.path.join('data', note))
    note_figure = pyg.transform.rotozoom(note_figure, 0,0.185)

    screen.blit(note_figure, (x,y))

#(width, height) = (int(GetSystemMetrics(0)), int(GetSystemMetrics(1)))
(width, height) = (900,600)
screen = pyg.display.set_mode((width, height))
screen.fill((255,255,225))
pyg.display.set_caption('Sheet Gen')
pyg.display.set_icon(screen)

i = 0
running = True

#def draw_sheet():
while running:
    pyg.event.get()
    #image settings
    g_clef = pyg.image.load(os.path.join('data', 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\g_clef.png'))
    g_clef = pyg.transform.rotozoom(g_clef, 0,0.185)
    #image settings

    #image prints
    screen.blit(g_clef, (i + 0,0))
    screen.blit(g_clef, (i + 0,100))
    screen.blit(g_clef, (i + 0,200))
    screen.blit(g_clef, (i + 0,300))
    screen.blit(g_clef, (i + 0,400))
    screen.blit(g_clef, (i + 0,500))
    i += 0.0
    #image prints

    #pentagrams
    pyg.draw.line(screen,(0,0,0), (20,20), (880,20), 1)
    pyg.draw.line(screen,(0,0,0), (20,35), (880,35), 1)
    pyg.draw.line(screen,(0,0,0), (20,50), (880,50), 1)
    pyg.draw.line(screen,(0,0,0), (20,65), (880,65), 1)
    pyg.draw.line(screen,(0,0,0), (20,80), (880,80), 1)

    pyg.draw.line(screen,(0,0,0), (20,120), (880,120), 1)
    pyg.draw.line(screen,(0,0,0), (20,135), (880,135), 1)
    pyg.draw.line(screen,(0,0,0), (20,150), (880,150), 1)
    pyg.draw.line(screen,(0,0,0), (20,165), (880,165), 1)
    pyg.draw.line(screen,(0,0,0), (20,180), (880,180), 1)

    pyg.draw.line(screen,(0,0,0), (20,220), (880,220), 1)
    pyg.draw.line(screen,(0,0,0), (20,235), (880,235), 1)
    pyg.draw.line(screen,(0,0,0), (20,250), (880,250), 1)
    pyg.draw.line(screen,(0,0,0), (20,265), (880,265), 1)
    pyg.draw.line(screen,(0,0,0), (20,280), (880,280), 1)

    pyg.draw.line(screen,(0,0,0), (20,320), (880,320), 1)
    pyg.draw.line(screen,(0,0,0), (20,335), (880,335), 1)
    pyg.draw.line(screen,(0,0,0), (20,350), (880,350), 1)
    pyg.draw.line(screen,(0,0,0), (20,365), (880,365), 1)
    pyg.draw.line(screen,(0,0,0), (20,380), (880,380), 1)

    pyg.draw.line(screen,(0,0,0), (20,420), (880,420), 1)
    pyg.draw.line(screen,(0,0,0), (20,435), (880,435), 1)
    pyg.draw.line(screen,(0,0,0), (20,450), (880,450), 1)
    pyg.draw.line(screen,(0,0,0), (20,465), (880,465), 1)
    pyg.draw.line(screen,(0,0,0), (20,480), (880,480), 1)

    pyg.draw.line(screen,(0,0,0), (20,520), (880,520), 1)
    pyg.draw.line(screen,(0,0,0), (20,535), (880,535), 1)
    pyg.draw.line(screen,(0,0,0), (20,550), (880,550), 1)
    pyg.draw.line(screen,(0,0,0), (20,565), (880,565), 1)
    pyg.draw.line(screen,(0,0,0), (20,580), (880,580), 1)
    #pentagrams

    #compass lines
    pyg.draw.line(screen,(0,0,0), (245,20), (245,80), 2)
    pyg.draw.line(screen,(0,0,0), (450,20), (450,80), 2)
    pyg.draw.line(screen,(0,0,0), (665,20), (665,80), 2)
    pyg.draw.line(screen,(0,0,0), (880,20), (880,80), 2)

    pyg.draw.line(screen,(0,0,0), (245,120), (245,180), 2)
    pyg.draw.line(screen,(0,0,0), (450,120), (450,180), 2)
    pyg.draw.line(screen,(0,0,0), (665,120), (665,180), 2)
    pyg.draw.line(screen,(0,0,0), (880,120), (880,180), 2)

    pyg.draw.line(screen,(0,0,0), (245,220), (245,280), 2)
    pyg.draw.line(screen,(0,0,0), (450,220), (450,280), 2)
    pyg.draw.line(screen,(0,0,0), (665,220), (665,280), 2)
    pyg.draw.line(screen,(0,0,0), (880,220), (880,280), 2)

    pyg.draw.line(screen,(0,0,0), (245,320), (245,380), 2)
    pyg.draw.line(screen,(0,0,0), (450,320), (450,380), 2)
    pyg.draw.line(screen,(0,0,0), (665,320), (665,380), 2)
    pyg.draw.line(screen,(0,0,0), (880,320), (880,380), 2)

    pyg.draw.line(screen,(0,0,0), (245,420), (245,480), 2)
    pyg.draw.line(screen,(0,0,0), (450,420), (450,480), 2)
    pyg.draw.line(screen,(0,0,0), (665,420), (665,480), 2)
    pyg.draw.line(screen,(0,0,0), (880,420), (880,480), 2)

    pyg.draw.line(screen,(0,0,0), (245,520), (245,580), 2)
    pyg.draw.line(screen,(0,0,0), (450,520), (450,580), 2)
    pyg.draw.line(screen,(0,0,0), (665,520), (665,580), 2)
    pyg.draw.line(screen,(0,0,0), (880,520), (880,580), 2)

    #compass lines

    #update image
    pyg.display.flip()
    #update image
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
