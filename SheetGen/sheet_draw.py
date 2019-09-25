import media as m
import pygame as pyg
import os
pos_x = 1366 / 2 - 900 / 2
pos_y = 768 - 600
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'
#from win32api import GetSystemMetrics

#(width, height) = (int(GetSystemMetrics(0)), int(GetSystemMetrics(1)))
(width, height) = (900,600)
screen = pyg.display.set_mode((width, height), pyg.RESIZABLE)
#sheet color
screen.fill((255,255,225))

icon = pyg.image.load(m.ico)

pyg.display.set_caption('Sheet Gen')
pyg.display.set_icon(icon)
pyg.display.init()

def draw_note_figure(note_figure, position_x, position_y, increase_point, resize_multiplier):
    #annotate the new note played
    note_figure = pyg.image.load(os.path.join('data', note_figure))
    note_figure = pyg.transform.rotozoom(note_figure, 0, resize_multiplier)
    screen.blit(note_figure, (position_x, position_y))
    #annotate the new note played

    #NOT IMPLEMENTED YET
    if increase_point:
        #annotate increase point
        note_figure = pyg.image.load(os.path.join('data', note_figure))
        note_figure = pyg.transform.rotozoom(note_figure, 0, resize_multiplier)
        screen.blit(note_figure, (position_x, position_y))
        #annotate increase point
    #update image
    pyg.display.flip()

def draw_tempo(tempo, compass):
    #60 24
    #75 25
    #90 26

    if(compass == 1):
        smn = pyg.image.load(os.path.join('data', m.seminima))
        smn = pyg.transform.rotozoom(smn, 0, 0.02)

        screen.blit(smn, (90,0))

    elif(compass == 2):
        smn = pyg.image.load(os.path.join('data', m.seminima))
        smn = pyg.transform.rotozoom(smn, 0, 0.02)

        dot = pyg.image.load(os.path.join('data', m.ponto))
        dot = pyg.transform.rotozoom(dot, 0, 0.007)

        screen.blit(smn, (85,0))
        screen.blit(dot, (97,11))

    else:
        pass

    if(tempo == 24):
        six_print = pyg.image.load(os.path.join('data', m.six))
        six_print = pyg.transform.rotozoom(six_print, 0, 0.025)

        zero_print = pyg.image.load(os.path.join('data', m.zero))
        zero_print = pyg.transform.rotozoom(zero_print, 0, 0.025)

        screen.blit(six_print, (103,3))
        screen.blit(zero_print, (110,3))

    elif(tempo == 25):
        seven_print = pyg.image.load(os.path.join('data', m.seven))
        seven_print = pyg.transform.rotozoom(seven_print, 0, 0.025)

        five_print = pyg.image.load(os.path.join('data', m.five))
        five_print = pyg.transform.rotozoom(five_print, 0, 0.025)

        screen.blit(seven_print, (103,3))
        screen.blit(five_print,  (110,3))

    elif(tempo == 26):
        nine_print = pyg.image.load(os.path.join('data', m.nine))
        nine_print = pyg.transform.rotozoom(nine_print, 0, 0.025)

        zero_print = pyg.image.load(os.path.join('data', m.zero))
        zero_print = pyg.transform.rotozoom(zero_print, 0, 0.025)

        screen.blit(nine_print, (103,3))
        screen.blit(zero_print,  (110,3))

        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
        os.environ['SDL_VIDEO_CENTERED'] = '0'


def draw_armor_clef(clef):

    #Dó  3
    #Sol 7
    #Fá  6

    if(clef == 3):
        return 45

    elif(clef == 7):
        g_major = pyg.image.load(os.path.join('data', m.sharp))
        g_major = pyg.transform.rotozoom(g_major, 0, 0.035)

        screen.blit(g_major, (63,9))
        screen.blit(g_major, (63,109))
        screen.blit(g_major, (63,209))
        screen.blit(g_major, (63,309))
        screen.blit(g_major, (63,409))
        screen.blit(g_major, (63,509))

        return 63
    elif(clef == 6):
        g_major = pyg.image.load(os.path.join('data', m.flat))
        g_major = pyg.transform.rotozoom(g_major, 0, 0.035)

        screen.blit(g_major, (60,31))
        screen.blit(g_major, (60,131))
        screen.blit(g_major, (60,231))
        screen.blit(g_major, (60,331))
        screen.blit(g_major, (60,431))
        screen.blit(g_major, (60,531))

        return 60

def draw_armor_compass(compass, distance):

    distance += 23

    #4/4 1
    #6/8 2

    if(compass == 1):

        quaternario = pyg.image.load(os.path.join('data', m.four))
        quaternario = pyg.transform.rotozoom(quaternario, 0, 0.046)

        #quatro
        screen.blit(quaternario, (distance,30))
        screen.blit(quaternario, (distance,130))
        screen.blit(quaternario, (distance,230))
        screen.blit(quaternario, (distance,330))
        screen.blit(quaternario, (distance,430))
        screen.blit(quaternario, (distance,530))
        #quatro
        screen.blit(quaternario, (distance,50))
        screen.blit(quaternario, (distance,150))
        screen.blit(quaternario, (distance,250))
        screen.blit(quaternario, (distance,350))
        screen.blit(quaternario, (distance,450))
        screen.blit(quaternario, (distance,550))

    elif(compass == 2):

        binario_composto_seis = pyg.image.load(os.path.join('data', m.six))
        binario_composto_oito = pyg.image.load(os.path.join('data', m.eight))
        binario_composto_seis = pyg.transform.rotozoom(binario_composto_seis, 0, 0.046)
        binario_composto_oito = pyg.transform.rotozoom(binario_composto_oito, 0, 0.046)

        #seis
        screen.blit(binario_composto_seis, (distance,30))
        screen.blit(binario_composto_seis, (distance,130))
        screen.blit(binario_composto_seis, (distance,230))
        screen.blit(binario_composto_seis, (distance,330))
        screen.blit(binario_composto_seis, (distance,430))
        screen.blit(binario_composto_seis, (distance,530))
        #oito
        screen.blit(binario_composto_oito, (distance,50))
        screen.blit(binario_composto_oito, (distance,150))
        screen.blit(binario_composto_oito, (distance,250))
        screen.blit(binario_composto_oito, (distance,350))
        screen.blit(binario_composto_oito, (distance,450))
        screen.blit(binario_composto_oito, (distance,550))

def draw_sheet():
#while running:
    #screen.fill((255,255,225))
    pyg.event.get()

    #image settings
    g_clef = pyg.image.load(os.path.join('data', m.g_clef))
    g_clef = pyg.transform.rotozoom(g_clef, 0, 0.185)
    #image settings

    #clef prints
    screen.blit(g_clef, (0,0))
    screen.blit(g_clef, (0,100))
    screen.blit(g_clef, (0,200))
    screen.blit(g_clef, (0,300))
    screen.blit(g_clef, (0,400))
    screen.blit(g_clef, (0,500))
    #clef prints

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

    #exit button does't work without loop ='(
    #so, I'm using no border window
    #for event in pyg.event.get():
    #    if event.type == pyg.QUIT:
    #        running = False
