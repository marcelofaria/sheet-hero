import pyaudio                  #auxilia na captação do áudio
import struct                   #converte os dados binarios captados do microfone
import numpy as np              #faz cálculos com as entradas do microfone
import matplotlib.pyplot as plt #plota gráficos
from scipy.fftpack import fft   #calculos com fast fourier transform
from tkinter import TclError    #trabalha com exceptions
import rules                    #meu módulo para definir notas e tempos
import sheet_draw as sd         #meu módulo para imprimir a partitura
import time                     #calcula o tempo das notas
import confirmation_box as cb   #
import pygame as pyg            #

def sheet_hero(compass, clef, tempo, title):
    #------------------- VARIABLES DECLARATION -------------------#
    #frames per buffer
    #the bigger the multiplier, the bigger the note accuracy
    #however, for reason of this performance loss, the note time accuracy decreases
    CHUNK    = 1024 * 1 #10 is ideal
    #quantity of bytes per sample
    FORMAT   = pyaudio.paInt16
    #mono or estereo
    CHANNELS = 1
    #quantity of samples grasp per second(audio quality)
    RATE     = 44100

    #two axis matplotlib and figure creation
    fig, (ax, ax2) = plt.subplots(2, figsize=(10,8))

    #pyaudio class instance
    p = pyaudio.PyAudio()

    #catches data of microphone
    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK)

    #variables to plot
    x = np.arange(0, 2 * CHUNK, 2)
    x_fft = np.linspace(0, RATE, CHUNK)

    #random data object
    line, = ax.plot(x, np.random.randn(CHUNK), '-', lw=2)
    #line_fft, = ax2.semilogx(x_fft, np.random.randn(CHUNK), '-', lw=2)
    line_fft, = ax2.plot(x_fft, np.random.randn(CHUNK), '-', lw=2)

    #axis formatting
    #--- Sound Waves ---#
    ax.set_title('Ondas Sonoras')
    ax.set_ylim(0, 255)   #limite do eixo y
    ax.set_xlim(0, CHUNK) #limite do eixo x
    plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0,128,255])
    #---   Spectrum   ---#
    ax2.set_title('Espectro')
    ax2.set_ylim(0, 0.9) #limite do eixo y
    ax2.set_xlim(0, 1600) #limite do eixo x
    #plt.setp(ax2, xticks=[500, 1000, 2000, 3000, 4000])
    #ax2.set_xlim(20, RATE/2)

    #shows the user interface of MATPLOTLIB
    #thismanager = plt.get_current_fig_manager()
    #thismanager.window.state('zoomed')

    #plt.show(block=False)
    #plt.summer()
    #loop utilities
    note              = ''          #initial declaration <> empty
    previous_note     = '1'         #initial declaration <> empty
    time_start        = 0           #initial declaration = 0 to count the time of the note
    movement          = 90          #
    note_x            = 0           #
    note_y            = 0           #
    pentagram_control = 1           #
    nomenclature      = ''          #
    noise_analysis    = 0           #
    noise_score       = 0
    one_time_var      = 0
    #------------------- VARIABLES DECLARATION -------------------#

    #-------------------     MAIN LOOP      -------------------#

    while True:

        sd.exit_system()
        #sd.generate_pdf()
        #retorna o tamanho em bytes da amostra captada
        data = stream.read(CHUNK)

        #converte o dado para inteiro
        data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

        #cria um vetor de numpy
        data_np = np.array(data_int, dtype='b')[::2] + 128
        line.set_ydata(data_np)

        #cria outro vetor de numpy
        #line_fft = class 'matplotlib.lines.Line2D'
        y_fft = fft(data_int)
        line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK))

        #x_data = class 'numpy.ndarray'
        x_data = line_fft.get_xdata(orig=False)
        y_data = line_fft.get_ydata(orig=False)
        xy_data = line_fft.get_xydata()

        sd.exit_system()
        #sd.generate_pdf()
        #--- CALCULA O PICO DO ESPECTRO ---#

        espectroVars = 0
        countI = 0
        #
        for i in np.nditer(xy_data):
            if countI > 10 and countI < 500:
                espectroVars = str(espectroVars) + "," + str(i)
            countI = countI + 1
        #
        splited = espectroVars
        splited = splited.split(",")
        splited = [float(y) for y in splited]

        even = 0
        x = 0

        odd = 0
        y = 1

        sd.exit_system()
        #sd.generate_pdf()
        #guarda em even os elementos pares da lista
        while x < len(splited):
            even = str(even) + "," + str(splited[x])
            x = x + 2

        splitedX = even.split(",")

        #tira o primeiro item adicionado pela atribuição inicial
        del splitedX[0]

        #guarda em odd os elementos impares da lista
        while y < len(splited):
            odd = str(odd) + "," + str(splited[y])
            y = y + 2

        splitedY = odd.split(",")

        #tira o primeiro item adicionado pela atribuição inicial
        del splitedY[0]

        #converte cada item do array de string pra float
        splitedY = [float(y) for y in splitedY]
        splitedX = [float(x) for x in splitedX]

        maxY = 0
        maxX = 0
        i = 0

        #retorna em maxX e maxY as coordenadas do pico da onda
        while i < len(splitedY):
            if splitedY[i] > maxY:
                maxY = splitedY[i]
                maxX = i
            i = i + 1
        sd.exit_system()
        #sd.generate_pdf()
        #print('X: ' + str(maxX))
        #print('Y: ' + str(maxY))

        #--- PRINTA O PICO DO ESPECTRO ---#

        #ann, = plt.plot(splitedX[maxX], maxY, '*', lw = 1)
        ann, = ax2.plot(splitedX[maxX], maxY, 'ro', lw = 1)
        #ann = ax2.annotate('*', xy=(splitedX[maxX] - 7 , maxY - 0.01 ))

        #--- IMPRIME O NOME E O SÍMBOLO DA NOTA TOCADA ---#
        note = rules.define_note(splitedX[maxX])

        if(noise_analysis <= 40):
            sd.print_noise_analysis(noise_analysis)
            if noise_analysis <= 2:
                pass
            elif total_time <= 0.25 and maxY >= 0.23 and (maxX <= 254 or maxX >= 959):
                noise_score += 1
                print('noise_score: ' + str(noise_score))
            if noise_score == 41:
                pyg.quit()
                cb.noise_mic()

            noise_analysis += 1
            movement = 90
        else:
            if(one_time_var == 0):
                sd.count_down()
                one_time_var += 1
            sd.draw_sheet()
            #sd.generate_pdf()
            distance = sd.draw_armor_clef(clef)
            sd.draw_armor_compass(compass, distance)
            sd.draw_tempo(tempo, compass)
            sd.draw_title(title)
            sd.exit_system()

        #note               : nota atual
        #previous_note      : nota anterior
        #time_start         : inicia a contagem do tempo
        #time_elapsed       : interrompe a contagem de tempo
        #total_time         : tempo passado entre mudança de notas
        #position_y_sheet   : definição da nota no pentagrama
        #nomenclature       : informa se é uma pausa ou uma nota
        #meio               : informa se a nota tocada precisa ser somada com colcheia
        #note_symbol        : controle para não avançar desnecessariamente na partitura
        #movement           : indice do eixo X para imprimir a nota no pygame
        #pentagram_control  : guarda o índice do pentagrama atual

        sd.exit_system()
        #sd.generate_pdf()
        if(note == previous_note):
            #print(note + ' ' + previous_note)
            pass
        else:
            time_elapsed = time.time()
            total_time = time_elapsed - time_start
            if(total_time > 0.19 and total_time < 64):
                position_y_sheet = rules.return_position_y(previous_note, pentagram_control)

                if(maxY < 0.2):
                    nomenclature = 'pauses'
                    position_y_sheet = rules.return_position_y_pause(pentagram_control)
                else:
                    aux_y = position_y_sheet
                    while aux_y > 14.5  :
                        aux_y -= 100
                    if(aux_y < 14.5 and aux_y > -32):
                        nomenclature = 'not_notes'
                    else:
                        nomenclature = 'notes'

                if (position_y_sheet != -1):
                    note_symbol = rules.note_figure(float(total_time), movement, position_y_sheet, 0.05, nomenclature)
                    #print(clef)
                    if (clef == 3 or clef == 7) and nomenclature != 'pauses':
                        #print('clef 45 ou 65')
                        if previous_note.find('#') != -1:
                            accidental = 'sharp'
                            #print('sharp')
                            rules.sharps_and_flats(accidental, movement, position_y_sheet)
                    if(note_symbol != 0.75 and note_symbol != 0.5 and note_symbol != 0.25 and type(note_symbol) == float):
                        if(note_symbol != 'Fora do tempo'):
                            if(movement >= 1220):
                                movement = 90
                                pentagram_control += 1
                            movement += 55
                    else:
                        if(movement >= 1230):
                                movement = 90
                                pentagram_control += 1
                        movement += 40
                    print(note, "%.2f" % (time_elapsed - time_start))
                    #print(note_symbol)
            time_start = time_elapsed

        previous_note = note
        sd.exit_system()
        #sd.generate_pdf()
        #movement += movement
        #fig.close()
        #updates the figure
        #try:
        #     fig.canvas.draw()
        #     fig.canvas.flush_events()
        #    ann.remove() #erases the wave peak annotation
        #except TclError:
        #     break

    #-------------------     MAIN LOOP      -------------------#
