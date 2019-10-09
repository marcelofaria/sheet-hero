import sheet_draw as sd         #meu módulo para imprimir a partitura
import media as m
import music_parameters as mp

def define_note(frequency_hz):
    #usar BUSCA BINARIA
    if(frequency_hz > 93.0 and frequency_hz < 190.6):
        if(frequency_hz > 93.0 and frequency_hz < 101.0):
            return ('Sol2')
        elif(frequency_hz > 101.1 and frequency_hz < 107.0):
            return ('Sol#2')
        elif(frequency_hz > 107.1 and frequency_hz < 113.0):
            return ('Lá2')
        elif(frequency_hz > 113.1 and frequency_hz < 119.0):
            return ('Lá#2')
        elif(frequency_hz > 119.1 and frequency_hz < 126.5):
            return ('Si2')
        #------------------------------------------------#
        elif(frequency_hz > 126.6 and frequency_hz < 133.9):
            return ('Dó3')
        elif(frequency_hz > 134.0 and frequency_hz < 142.0):
            return ('Dó#3')
        elif(frequency_hz > 142.1 and frequency_hz < 150.0):
            return ('Ré3')
        elif(frequency_hz > 150.1 and frequency_hz < 159.5):
            return ('Ré#3')
        elif(frequency_hz > 159.6 and frequency_hz < 168.9):
            return ('Mi3')
        elif(frequency_hz > 169.0 and frequency_hz < 179.0):
            return ('Fá3')
        elif(frequency_hz > 179.1 and frequency_hz < 190.5):
            return ('Fá#3')
    elif(frequency_hz > 190.5 and frequency_hz < 678.0):
        if(frequency_hz > 190.6 and frequency_hz < 201.5):
            return ('Sol3')
        elif(frequency_hz > 201.6 and frequency_hz < 212.5):
            return ('Sol#3')
        elif(frequency_hz > 212.6 and frequency_hz < 226.5):
            return ('Lá3')
        elif(frequency_hz > 226.6 and frequency_hz < 239.9):
            return ('Lá#3')
        elif(frequency_hz > 240.0 and frequency_hz < 254.0):
            return ('Si3')
        #------------------------------------------------#
        elif(frequency_hz > 254.1 and frequency_hz < 268.9):
            return ('Dó4')
        elif(frequency_hz > 269.0 and frequency_hz < 284.9):
            return ('Dó#4')
        elif(frequency_hz > 285.0 and frequency_hz < 301.9):
            return ('Ré4')
        elif(frequency_hz > 302.0 and frequency_hz < 320.0):
            return ('Ré#4')
        elif(frequency_hz > 320.1 and frequency_hz < 338.9):
            return ('Mi4')
        elif(frequency_hz > 339.0 and frequency_hz < 359.0):
            return ('Fá4')
        elif(frequency_hz > 359.1 and frequency_hz < 380.9):
            return ('Fá#4')
        elif(frequency_hz > 381.0 and frequency_hz < 403.0):
            return ('Sol4')
        elif(frequency_hz > 403.1 and frequency_hz < 426.9):
            return ('Sol#4')
        elif(frequency_hz > 427.0 and frequency_hz < 452.9):
            return ('Lá4')
        elif(frequency_hz > 453.0 and frequency_hz < 479.9):
            return ('Lá#4')
        elif(frequency_hz > 480.0 and frequency_hz < 508.0):
            return ('Si4')
        #------------------------------------------------#
        #------------------------------------------------#
        elif(frequency_hz > 508.1 and frequency_hz < 537.9):
            return ('Dó5')
        elif(frequency_hz > 538.0 and frequency_hz < 569.9):
            return ('Dó#5')
        elif(frequency_hz > 570.0 and frequency_hz < 603.9):
            return ('Ré5')
        elif(frequency_hz > 604.0 and frequency_hz < 639.9):
            return ('Ré#5')
        elif(frequency_hz > 640.0 and frequency_hz < 677.9):
            return ('Mi5')
    elif(frequency_hz > 677.9 and frequency_hz < 1612.1):
        if(frequency_hz > 678.0 and frequency_hz < 717.9):
            return ('Fá5')
        elif(frequency_hz > 718.0 and frequency_hz < 759.9):
            return ('Fá#5')
        elif(frequency_hz > 760.0 and frequency_hz < 806.9):
            return ('Sol5')
        elif(frequency_hz > 807.0 and frequency_hz < 853.9):
            return ('Sol#5')
        elif(frequency_hz > 854.0 and frequency_hz < 905.9):
            return ('Lá5')
        elif(frequency_hz > 906.0 and frequency_hz < 958.9):
            return ('Lá#5')
        elif(frequency_hz > 959.0 and frequency_hz < 1014.9):
            return ('Si5')
        #------------------------------------------------#
        #------------------------------------------------#
        elif(frequency_hz > 1015.0 and frequency_hz < 1075.9):
            return ('Dó6')
        elif(frequency_hz > 1076.0 and frequency_hz < 1139.9):
            return ('Dó#6')
        elif(frequency_hz > 1140.0 and frequency_hz < 1207.9):
            return ('Ré6')
        elif(frequency_hz > 1208.0 and frequency_hz < 1279.9):
            return ('Ré#6')
        elif(frequency_hz > 1280.0 and frequency_hz < 1355.9):
            return ('Mi6')
        elif(frequency_hz > 1356.0 and frequency_hz < 1435.9):
            return ('Fá6')
        elif(frequency_hz > 1436.0 and frequency_hz < 1522.9):
            return ('Fá#6')
        elif(frequency_hz > 1523.0 and frequency_hz < 1612.0):
            return ('Sol6')
    #------------------------------------------------#
    else:
        return ('Fora do limite')

def note_figure(time_elapsed, x, y, resize_multiplier, nomenclature):
    # notas
    if(nomenclature == 'notes'):
        # 4 tempos semibreve
        if (time_elapsed >= 3.75 and time_elapsed <= 4.25):
            sd.draw_note_figure(m.semibreve, x, y, False, resize_multiplier - 0.025)
            return (4)
        # 3,5 tempos minima pontuada com colcheia
        elif(time_elapsed >= 3.26 and time_elapsed <= 3.74):
            sd.draw_note_figure(m.minima, x - 15, y, False, resize_multiplier + 0.007)
            sd.draw_note_figure(m.ponto, x + 16, y + 33, False, resize_multiplier - 0.04)
            sd.draw_note_figure(m.colcheia, x + 15, y, False, resize_multiplier)
            sd.draw_note_figure(m.ligature, x + 8, y + 25, False, resize_multiplier - 0.033)
            return(3.5)
        # 3 tempos minima
        elif (time_elapsed >= 2.75 and time_elapsed <= 3.25):
            sd.draw_note_figure(m.minima, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (3)
        # 2,5 tempos minima com colcheia
        elif(time_elapsed >= 2.26 and time_elapsed <= 2.74):
            sd.draw_note_figure(m.minima, x - 15, y, False, resize_multiplier + 0.007)
            sd.draw_note_figure(m.colcheia, x + 15, y, False, resize_multiplier)
            sd.draw_note_figure(m.ligature, x + 8, y + 25, False, resize_multiplier - 0.033)
            return(2.5)
        # 2 tempos minima
        elif (time_elapsed >= 1.75 and time_elapsed <= 2.25):
            sd.draw_note_figure(m.minima, x, y, False, resize_multiplier)
            return (2)
        # 1,5 tempos seminima pontuada
        elif (time_elapsed >= 1.25 and time_elapsed <= 1.75):
            sd.draw_note_figure(m.seminima, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (1.5)
        # 1 tempo seminima
        elif (time_elapsed >= 0.76 and time_elapsed <= 1.24):
            sd.draw_note_figure(m.seminima, x, y, False, resize_multiplier)
            return (1)
        # 0,75 tempo colcheia pontuada
        elif (time_elapsed >= 0.71 and time_elapsed <= 0.75):
            sd.draw_note_figure(m.colcheia, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (0.75)
        # 0,5 tempo colcheia
        elif (time_elapsed >= 0.3 and time_elapsed <= 0.70):
            sd.draw_note_figure(m.colcheia, x, y, False, resize_multiplier)
            return (0.5)
        # 0,25 tempo semicolcheia
        elif (time_elapsed >= 0.2 and time_elapsed <= 0.29):
            sd.draw_note_figure(m.semicolcheia, x, y, False, resize_multiplier)
            return (0.25)
    # pausas
    elif(nomenclature == 'pauses'):
        # 4 tempos semibreve
        if (time_elapsed >= 3.75 and time_elapsed <= 4.25):
            sd.draw_note_figure(m.p_semibreve, x, y, False, resize_multiplier - 0.008)
            return (4)
        # 3,5 tempos minima pontuada com colcheia
        elif(time_elapsed >= 3.26 and time_elapsed <= 3.74):
            sd.draw_note_figure(m.p_minima, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            sd.draw_note_figure(m.p_colcheia, x, y + 5, False, resize_multiplier)
            return(3.5)
        # 3 tempos minima
        elif (time_elapsed >= 2.75 and time_elapsed <= 3.25):
            sd.draw_note_figure(m.p_minima, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (3)
        # 2,5 tempos minima com colcheia
        elif(time_elapsed >= 2.26 and time_elapsed <= 2.74):
            sd.draw_note_figure(m.p_minima, x, y, False, resize_multiplier)
            #sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier)
            sd.draw_note_figure(m.p_colcheia, x, y + 5, False, resize_multiplier)
            return(2.5)
        # 2 tempos minima
        elif (time_elapsed >= 1.75 and time_elapsed <= 2.25):
            sd.draw_note_figure(m.p_minima, x, y, False, resize_multiplier)
            return (2)
        # 1,5 tempos seminima pontuada
        elif (time_elapsed >= 1.25 and time_elapsed <= 1.75):
            sd.draw_note_figure(m.p_seminima, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (1.5)
        # 1 tempo seminima
        elif (time_elapsed >= 0.76 and time_elapsed <= 1.24):
            sd.draw_note_figure(m.p_seminima, x, y, False, resize_multiplier)
            return (1)
        # 0,75 tempo colcheia pontuada
        elif (time_elapsed >= 0.71 and time_elapsed <= 0.75):
            sd.draw_note_figure(m.p_colcheia, x, y, False, resize_multiplier)
            sd.draw_note_figure(m.ponto, x, y + 3, False, resize_multiplier - 0.04)
            return (0.75)
        # 0,5 tempo colcheia
        elif (time_elapsed >= 0.3 and time_elapsed <= 0.70):
            sd.draw_note_figure(m.p_colcheia, x, y, False, resize_multiplier)
            return (0.5)
        # 0,25 tempo semicolcheia
        elif (time_elapsed >= 0.2 and time_elapsed <= 0.29):
            sd.draw_note_figure(m.p_colcheia, x, y, False, resize_multiplier)
            return (0.25)
    else:
        return('Fora do tempo')

def return_position_y_pause(pentagram):
    axis_y_pentagram = 37.5
    if(pentagram == 2):
        axis_y_pentagram += 100
        return axis_y_pentagram
    elif(pentagram == 3):
        axis_y_pentagram += 200
        return axis_y_pentagram
    elif(pentagram == 4):
        axis_y_pentagram += 300
        return axis_y_pentagram
    elif(pentagram == 5):
        axis_y_pentagram += 400
        return axis_y_pentagram
    elif(pentagram == 6):
        axis_y_pentagram += 500
        return axis_y_pentagram
    elif(pentagram > 7):
        axis_y_pentagram = -100000000
        return axis_y_pentagram
    else:
        return axis_y_pentagram

def return_position_y(note, pentagram):
    #axis_y_pentagram = 0
    if  (note == 'Si5'):
        axis_y_pentagram = -40.5
    elif(note == 'Lá#5'):
        axis_y_pentagram = -32.5
    elif(note == 'Lá5'):
        axis_y_pentagram = -32.5
    elif(note == 'Sol#5'):
        axis_y_pentagram = -24.5
    elif(note == 'Sol5'):
        axis_y_pentagram = -24.5
    elif(note == 'Fá#5'):
        axis_y_pentagram = -16.5
    elif(note == 'Fá5'):
        axis_y_pentagram = -16.5
    elif(note == 'Mi5'):
        axis_y_pentagram = -8.5
    elif(note == 'Ré#5'):
        axis_y_pentagram = -1.5
    elif(note == 'Ré5'):
        axis_y_pentagram = -1.5
    elif(note == 'Dó#5'):
        axis_y_pentagram = 7.5
    elif(note == 'Dó5'):
        axis_y_pentagram = 7.5
    elif(note == 'Si4'):
        axis_y_pentagram = 15.5
    elif(note == 'Lá#4'):
        axis_y_pentagram = 23.5
    elif(note == 'Lá4'):
        axis_y_pentagram = 23.5
    elif(note == 'Sol#4'):
        axis_y_pentagram = 31.5
    elif(note == 'Sol4'):
        axis_y_pentagram = 31.5
    elif(note == 'Fá#4'):
        axis_y_pentagram = 39.5
    elif(note == 'Fá4'):
        axis_y_pentagram = 39.5
    elif(note == 'Mi4'):
        axis_y_pentagram = 47.5
    elif(note == 'Ré#4'):
        axis_y_pentagram = 55.5
    elif(note == 'Ré4'):
        axis_y_pentagram = 55.5
    elif(note == 'Dó#4'):
        axis_y_pentagram = 63.5
    elif(note == 'Dó4'):
        axis_y_pentagram = 63.5
    elif(note == 'Si3'):
        axis_y_pentagram = 70.5
    else:
        axis_y_pentagram = -100000000

    if(pentagram == 2):
        axis_y_pentagram += 100
        return axis_y_pentagram
    elif(pentagram == 3):
        axis_y_pentagram += 200
        return axis_y_pentagram
    elif(pentagram == 4):
        axis_y_pentagram += 300
        return axis_y_pentagram
    elif(pentagram == 5):
        axis_y_pentagram += 400
        return axis_y_pentagram
    elif(pentagram == 6):
        axis_y_pentagram += 500
        return axis_y_pentagram
    elif(pentagram > 6):
        axis_y_pentagram = -1
        return axis_y_pentagram
    else:
        return axis_y_pentagram
