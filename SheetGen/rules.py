import sheet_draw as sd         #meu módulo para imprimir a partitura

semibreve     = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\semibreve.png'      #path
minima        = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\minima.png'         #path
seminima      = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\seminima.png'       #path
colcheia      = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\colcheia.png'       #path
semicolcheia  = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\semicolcheia.png'   #path
fusa          = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\fusa.png'           #path
semifusa      = 'C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\Media\\semifusa.png'       #path

def define_note(frequency_hz):
    #usar BUSCA BINARIA
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
    elif(frequency_hz > 190.6 and frequency_hz < 201.5):
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
    elif(frequency_hz > 678.0 and frequency_hz < 717.9):
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

def note_figure(time_elapsed, x, y, resize_multiplier):
    if (time_elapsed >= 3.8 and time_elapsed <= 4.2):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('SEMIBREVE 𝅝 4 tempos')
    elif (time_elapsed >= 2.8 and time_elapsed <= 3.2):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('MINIMA. 𝅗𝅥. 3 tempos')
    elif (time_elapsed >= 1.8 and time_elapsed <= 2.2):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('MINIMA 𝅗𝅥 2 tempos')
    elif (time_elapsed >= 1.3 and time_elapsed <= 1.7):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('SEMINIMA. ♩. 1.5 tempos')
    elif (time_elapsed >= 0.8 and time_elapsed <= 1.2):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('SEMINIMA ♩ 1 tempo')
    elif (time_elapsed >= 0.71 and time_elapsed <= 0.79):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('COLCHEIA. 𝅘𝅥𝅮. 0.75 tempo')
    elif (time_elapsed >= 0.3 and time_elapsed <= 0.7):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('COLCHEIA 𝅘𝅥𝅮 0.5 tempo')
    elif (time_elapsed >= 0.2 and time_elapsed <= 0.29):
        sd.draw_note_figure(colcheia, x, y, False, resize_multiplier)
        return ('SEMICOLCHEIA 𝅘𝅥𝅯 0.25 tempo')

    else:
        return('Fora do tempo')

def return_position_y(note):
    if(note   == 'Mi5'):
        return -8.5
    elif(note == 'Ré5'):
        return -1.5
    elif(note == 'Dó5'):
        return 7.5
    elif(note == 'Si4'):
        return 14.5
    elif(note == 'Lá4'):
        return 22.5
    elif(note == 'Sol4'):
        return 29.5
    elif(note == 'Fá4'):
        return 37.5
    elif(note == 'Mi4'):
        return 44.5
    elif(note == 'Ré4'):
        return 52.5
    else:
        return -100
