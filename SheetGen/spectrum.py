import pyaudio                  #auxilia na captação do áudio
import struct                   #converte os dados binarios captados do microfone
import numpy as np              #faz cálculos com as entradas do microfone
import matplotlib.pyplot as plt #plota gráficos
from scipy.fftpack import fft   #calculos com fast fourier transform
from tkinter import TclError    #trabalha com exceptions
import rules                    #meu módulo para definir notas e tempos
import sheet_draw as sd         #meu módulo para imprimir a partitura
import time                     #calcula o tempo das notas

def sheet_hero(compass, clef):
    #------------------- VARIABLES DECLARATION -------------------#

    #frames per buffer
    #the bigger the multiplier, the bigger the note grasp accuracy
    #however, for reason of this performance loss, the note time accuracy decreases
    CHUNK    = 1024 * 10 #10 is ideal
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
    ax2.set_ylim(0, 0.85) #limite do eixo y
    ax2.set_xlim(0, 1600) #limite do eixo x
    #plt.setp(ax2, xticks=[500, 1000, 2000, 3000, 4000])
    #ax2.set_xlim(20, RATE/2)

    #shows the user interface of MATPLOTLIB
    thismanager = plt.get_current_fig_manager()
    thismanager.window.state('zoomed')

    plt.show(block=False)
    #plt.summer()
    #loop utilities
    note              = ''          #initial declaration <> empty
    previous_note     = '1'         #initial declaration <> empty
    time_start        = 0           #initial declaration = 0 to count the time of the note
    movement          = 75          #fluidity test
    note_x            = 0           #
    note_y            = 0           #
    pentagram_control = 1           #
    #------------------- VARIABLES DECLARATION -------------------#

    #-------------------     MAIN LOOP      -------------------#

    while True:
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

        #--- PRINTA O PICO DO ESPECTRO ---#

        #ann, = plt.plot(splitedX[maxX], maxY, '*', lw = 1)
        ann, = ax2.plot(splitedX[maxX], maxY, 'ro', lw = 1)
        #ann = ax2.annotate('*', xy=(splitedX[maxX] - 7 , maxY - 0.01 ))

        #--- IMPRIME O NOME E O SÍMBOLO DA NOTA TOCADA ---#
        note = rules.define_note(splitedX[maxX])

        if(note == previous_note):
            #print(note + ' ' + previous_note)
            pass
        else:
            time_elapsed = time.time()
            total_time = time_elapsed - time_start
            if(total_time > 0.19 and total_time < 64):
                position_y_sheet = rules.return_position_y(note, pentagram_control)
                note_symbol = rules.note_figure(float(total_time), movement , position_y_sheet, 0.05)
                if(note_symbol != 'Fora do tempo'):
                    if(movement >= 830):
                        movement = 75
                        pentagram_control += 1
                    movement += 20
                print(note, "%.2f" % (time_elapsed - time_start))
                print(note_symbol)
            time_start = time_elapsed

        previous_note = note

        sd.draw_sheet()
        distance = sd.draw_armor_clef(clef)
        sd.draw_armor_compass(compass, distance)


        #movement += movement

        #updates the figure
        try:
            #fig.canvas.draw()
            fig.canvas.flush_events()
            #ann.remove() #erases the wave peak annotation
        except TclError:
            break

    #-------------------     MAIN LOOP      -------------------#

    #-- TASKS --#
    #FEITO - IMPLEMENTAR VERIFICAÇÃO PARA MUDAR DE PENTAGRAMA QUANDO O ATUAL FOR COMPLETAMENTE PREENCHIDO
    #FEITO - IMPLEMENTAR SISTEMA DE CONFIGURAÇÃO INICIAL COM INTERFACE GRÁFICA
        #FEITO - IMPLEMENTAR CONFIGURAÇÃO DE ARMADURA DE CLAVE
        #FEITO - IMPLEMENTAR CONFIGURAÇÃO DE ARMADURA DE COMPASSO
        #IMPLEMENTAR CONFIGURAÇÃO DE ANDAMENTO (BPM)
    #IMPLEMENTAR INTELIGÊNCIA DE PREENCHIMENTO DE COMPASSOS BASEADOS NA ARMADURA DE CLAVE - PRECISO PENSAR
    #IMPLEMENTAR INTELIGÊNCIA DE DISTÂNCIA ENTRE NOTAS PARA PREENCHIMENTO DO COMPASSO - DA PRA FAZER
    #IMPLEMENTAR SISTEMA QUE DETERMINA OS RANGES DE TEMPOS DAS NOTAS BASEADO NO BPM INSERIDO - CONSULTAR BPM CALCULATOR
    #IMPLEMENTAR INTELIGÊNCIA PARA RESOLVER OS 'Fora do tempo'. NÃO DEVE EXISTIR NENHUM 'Fora do tempo'. QUALQUER TEMPO É PASSÍVEL DE REPRESENTAÇÃO
        #IMPLEMENTAR SISTEMA DE LIGADURAS PARA RESOLVER O PROBLEMA ACIMA
    #IMPLEMENTAR CONFIGURAÇÃO PARA TÍTULO E INFORMAÇÕES DA PARTITURA
    #FEITO - CONSERTAR O POSICIONAMENTO DA JANELA QUANDO INICIAR O SISTEMA
    #REDIMENSIONAR A

    #-- PROBLEMAS --#
    #SE A MESMA NOTA FOR TOCADA VÁRIAS VEZES, O ALGORITMO VAI CONSIDERAR COMO UMA VEZ =( - FERROU
        #POSSÍVEL SOLUÇÃO
        #ANALISAR ALTURA DA ONDA PARA IDENTIFICAR AS TRANSIÇÕES
    #ALGUMAS NOTAS AINDA ESTÃO SENDO DESENHADAS MAIS DISTANTES
        #VERIFICAR AS NOTAS QUE NÃO FORAM CATEGORIZADAS E AS ACIDENTADAS
