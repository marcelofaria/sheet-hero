import media as m
import pygame as pyg
import os
import time
import sys
from fpdf import FPDF
#from win32api import GetSystemMetrics

pdf = FPDF(orientation = 'L', unit = 'pt', format = (780, 1335))
pos_x = 1366 / 2 - 1280 / 2
pos_y = 768 - 720
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

#(width, height) = (int(GetSystemMetrics(0)), int(GetSystemMetrics(1)))
(width, height) = (1280, 720)
screen = pyg.display.set_mode((width, height))
button = pyg.Rect(1200, 50, 100, 50)
#pyg.transform.smoothscale(screen, (width//10, height//10))
#sheet color
screen.fill((255,255,225))

icon = pyg.image.load(m.ico)

#global xy vars
start = 20
end   = 1260
plus  = 90

pyg.display.set_icon(icon)
pyg.display.init()

def draw_title(title):
    number = len(title)

    title_y = 630 - (number * 10)

    pyg.display.set_caption(title)
    pyg.font.init() # you have to call this at the start,
                    # if you want to use this module.
    my_font = pyg.font.SysFont('Calibri', 50)
    #my_font.set_bold(True)
    text_surface = my_font.render(title, False, (0, 0, 0))
    screen.blit(text_surface,(title_y,25))

def draw_note_figure(note_figure, position_x, position_y, increase_point, resize_multiplier):
    #annotate the new note played
    note_figure = pyg.image.load(os.path.join('data', note_figure))
    note_figure = pyg.transform.rotozoom(note_figure, 0, resize_multiplier)
    screen.blit(note_figure, (position_x, position_y + plus))
    #annotate the new note played

    #NOT IMPLEMENTED YET
    if increase_point:
        #annotate increase point
        note_figure = pyg.image.load(os.path.join('data', note_figure))
        note_figure = pyg.transform.rotozoom(note_figure, 0, resize_multiplier)
        screen.blit(note_figure, (position_x, position_y + plus))
        #annotate increase point
    #update image
    pyg.display.flip()
    generate_pdf()

def generate_pdf():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()
        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                filename = m.insert_filename('Generated_Sheet')
                pyg.image.save(screen, filename)
                pdf.add_page()
                pdf.image(filename)
                pdf.output(m.filename_pdf, "F")

def draw_tempo(tempo, compass):
    #60 24
    #75 25
    #90 26

    if(compass == 1):
        smn = pyg.image.load(os.path.join('data', m.seminima))
        smn = pyg.transform.rotozoom(smn, 0, 0.02)

        screen.blit(smn, (90,0 + plus))

    elif(compass == 2):
        smn = pyg.image.load(os.path.join('data', m.seminima))
        smn = pyg.transform.rotozoom(smn, 0, 0.02)

        dot = pyg.image.load(os.path.join('data', m.ponto))
        dot = pyg.transform.rotozoom(dot, 0, 0.007)

        screen.blit(smn, (85,0 + plus))
        screen.blit(dot, (97,11 + plus))

    else:
        pass

    if(tempo == 24):
        six_print = pyg.image.load(os.path.join('data', m.six))
        six_print = pyg.transform.rotozoom(six_print, 0, 0.025)

        zero_print = pyg.image.load(os.path.join('data', m.zero))
        zero_print = pyg.transform.rotozoom(zero_print, 0, 0.025)

        screen.blit(six_print, (103,3 + plus))
        screen.blit(zero_print, (110,3 + plus))

    elif(tempo == 25):
        seven_print = pyg.image.load(os.path.join('data', m.seven))
        seven_print = pyg.transform.rotozoom(seven_print, 0, 0.025)

        five_print = pyg.image.load(os.path.join('data', m.five))
        five_print = pyg.transform.rotozoom(five_print, 0, 0.025)

        screen.blit(seven_print, (103,3 + plus))
        screen.blit(five_print,  (110,3 + plus))

    elif(tempo == 26):
        nine_print = pyg.image.load(os.path.join('data', m.nine))
        nine_print = pyg.transform.rotozoom(nine_print, 0, 0.025)

        zero_print = pyg.image.load(os.path.join('data', m.zero))
        zero_print = pyg.transform.rotozoom(zero_print, 0, 0.025)

        screen.blit(nine_print, (103,3 + plus))
        screen.blit(zero_print,  (110,3 + plus))

        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
        os.environ['SDL_VIDEO_CENTERED'] = '0'

        generate_pdf()

def draw_armor_clef(clef):

    #Dó  3
    #Sol 7
    #Fá  6

    if(clef == 3):
        return 45

    elif(clef == 7):
        g_major = pyg.image.load(os.path.join('data', m.sharp))
        g_major = pyg.transform.rotozoom(g_major, 0, 0.035)

        screen.blit(g_major, (63,9 + plus))
        screen.blit(g_major, (63,109 + plus))
        screen.blit(g_major, (63,209 + plus))
        screen.blit(g_major, (63,309 + plus))
        screen.blit(g_major, (63,409 + plus))
        screen.blit(g_major, (63,509 + plus))

        return 63
    elif(clef == 6):
        g_major = pyg.image.load(os.path.join('data', m.flat))
        g_major = pyg.transform.rotozoom(g_major, 0, 0.035)

        screen.blit(g_major, (60,31 + plus))
        screen.blit(g_major, (60,131 + plus))
        screen.blit(g_major, (60,231 + plus))
        screen.blit(g_major, (60,331 + plus))
        screen.blit(g_major, (60,431 + plus))
        screen.blit(g_major, (60,531 + plus))

        return 60

def draw_armor_compass(compass, distance):

    distance += 23

    #4/4 1
    #6/8 2

    if(compass == 1):

        quaternario = pyg.image.load(os.path.join('data', m.four))
        quaternario = pyg.transform.rotozoom(quaternario, 0, 0.046)

        #quatro
        screen.blit(quaternario, (distance,30 + plus))
        screen.blit(quaternario, (distance,130 + plus))
        screen.blit(quaternario, (distance,230 + plus))
        screen.blit(quaternario, (distance,330 + plus))
        screen.blit(quaternario, (distance,430 + plus))
        screen.blit(quaternario, (distance,530 + plus))
        #quatro
        screen.blit(quaternario, (distance,50 + plus))
        screen.blit(quaternario, (distance,150 + plus))
        screen.blit(quaternario, (distance,250 + plus))
        screen.blit(quaternario, (distance,350 + plus))
        screen.blit(quaternario, (distance,450 + plus))
        screen.blit(quaternario, (distance,550 + plus))

    elif(compass == 2):

        binario_composto_seis = pyg.image.load(os.path.join('data', m.six))
        binario_composto_oito = pyg.image.load(os.path.join('data', m.eight))
        binario_composto_seis = pyg.transform.rotozoom(binario_composto_seis, 0, 0.046)
        binario_composto_oito = pyg.transform.rotozoom(binario_composto_oito, 0, 0.046)

        #seis
        screen.blit(binario_composto_seis, (distance,30 + plus))
        screen.blit(binario_composto_seis, (distance,130 + plus))
        screen.blit(binario_composto_seis, (distance,230 + plus))
        screen.blit(binario_composto_seis, (distance,330 + plus))
        screen.blit(binario_composto_seis, (distance,430 + plus))
        screen.blit(binario_composto_seis, (distance,530 + plus))
        #oito
        screen.blit(binario_composto_oito, (distance,50 + plus))
        screen.blit(binario_composto_oito, (distance,150 + plus))
        screen.blit(binario_composto_oito, (distance,250 + plus))
        screen.blit(binario_composto_oito, (distance,350 + plus))
        screen.blit(binario_composto_oito, (distance,450 + plus))
        screen.blit(binario_composto_oito, (distance,550 + plus))

        generate_pdf()

def count_down():
    i = 1
    while i > 0:

        time.sleep(1)
        title_y = 630 - (2 * 10)
        pyg.font.init() # you have to call this at the start,
                        # if you want to use this module.
        my_font = pyg.font.SysFont('Calibri', 50)
        #my_font.set_bold(True)
        text_surface = my_font.render(str(i), False, (0, 0, 0))
        screen.blit(text_surface,(title_y,25))
        #update image
        pyg.display.flip()
        #update image
        screen.fill((255,255,225))
        i -= 1

def draw_sheet():
#while running:
    pyg.event.get()

    pyg.draw.rect(screen, [154, 160, 171], button)

    #image settings
    g_clef = pyg.image.load(os.path.join('data', m.g_clef))
    g_clef = pyg.transform.rotozoom(g_clef, 0, 0.185)
    #image settings

    #clef prints
    screen.blit(g_clef, (0,0 + plus))
    screen.blit(g_clef, (0,100 + plus))
    screen.blit(g_clef, (0,200 + plus))
    screen.blit(g_clef, (0,300 + plus))
    screen.blit(g_clef, (0,400 + plus))
    screen.blit(g_clef, (0,500 + plus))
    #clef prints

    #pentagrams
    pyg.draw.line(screen,(0,0,0), (start,20 + plus), (end,20 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,35 + plus), (end,35 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,50 + plus), (end,50 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,65 + plus), (end,65 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,80 + plus), (end,80 + plus), 1)

    pyg.draw.line(screen,(0,0,0), (start,120 + plus), (end,120 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,135 + plus), (end,135 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,150 + plus), (end,150 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,165 + plus), (end,165 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,180 + plus), (end,180 + plus), 1)

    pyg.draw.line(screen,(0,0,0), (start,220 + plus), (end,220 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,235 + plus), (end,235 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,250 + plus), (end,250 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,265 + plus), (end,265 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,280 + plus), (end,280 + plus), 1)

    pyg.draw.line(screen,(0,0,0), (start,320 + plus), (end,320 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,335 + plus), (end,335 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,350 + plus), (end,350 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,365 + plus), (end,365 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,380 + plus), (end,380 + plus), 1)

    pyg.draw.line(screen,(0,0,0), (start,420 + plus), (end,420 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,435 + plus), (end,435 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,450 + plus), (end,450 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,465 + plus), (end,465 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,480 + plus), (end,480 + plus), 1)

    pyg.draw.line(screen,(0,0,0), (start,520 + plus), (end,520 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,535 + plus), (end,535 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,550 + plus), (end,550 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,565 + plus), (end,565 + plus), 1)
    pyg.draw.line(screen,(0,0,0), (start,580 + plus), (end,580 + plus), 1)
    #pentagrams

    #compass lines
    pyg.draw.line(screen,(0,0,0), (285,20 + plus), (285,80 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,20 + plus), (523,80 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,20 + plus), (761,80 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,20 + plus), (999,80 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,20 + plus), (1260,80 + plus), 2)

    pyg.draw.line(screen,(0,0,0), (285,120 + plus), (285,180 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,120 + plus), (523,180 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,120 + plus), (761,180 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,120 + plus), (999,180 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,120 + plus), (1260,180 + plus), 2)

    pyg.draw.line(screen,(0,0,0), (285,220 + plus), (285,280 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,220 + plus), (523,280 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,220 + plus), (761,280 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,220 + plus), (999,280 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,220 + plus), (1260,280 + plus), 2)

    pyg.draw.line(screen,(0,0,0), (285,320 + plus), (285,380 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,320 + plus), (523,380 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,320 + plus), (761,380 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,320 + plus), (999,380 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,320 + plus), (1260,380 + plus), 2)

    pyg.draw.line(screen,(0,0,0), (285,420 + plus), (285,480 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,420 + plus), (523,480 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,420 + plus), (761,480 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,420 + plus), (999,480 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,420 + plus), (1260,480 + plus), 2)

    pyg.draw.line(screen,(0,0,0), (285,520 + plus), (285,580 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (523,520 + plus), (523,580 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (761,520 + plus), (761,580 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (999,520 + plus), (999,580 + plus), 2)
    pyg.draw.line(screen,(0,0,0), (1260,520 + plus), (1260,580 + plus), 2)
    #compass lines

    #update image
    pyg.display.flip()
    #update image

    #colocar a main dentro desse for e testar se o botão fechar funciona
    #main dentro de for? é, eu não sei como fazer isso

    #exit button does't work without loop ='(
    #so, I'm using no border window
    generate_pdf()
