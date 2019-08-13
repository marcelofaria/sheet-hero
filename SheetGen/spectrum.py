import pyaudio                  #auxilia na captação do áudio
import struct                   #converte os dados binarios captados do microfone
import numpy as np              #faz cálculos com as entradas do microfone
import matplotlib.pyplot as plt #plota gráficos
from scipy.fftpack import fft   #calculos com fast fourier transform
from tkinter import TclError    #trabalha com exceptions
import rules                    #meu módulo de funções utilitárias
import time                     #calcula o tempo das notas

#------------------- DECLARAÇÃO DE VARIÁVEIS -------------------#

#quadros por buffer
CHUNK = 1024 * 6

#quantidade de bytes por amostra
FORMAT = pyaudio.paInt16

#mono ou estéreo
CHANNELS = 1

#quantidade de amostras captadas por segundo (qualidade do áudio)
RATE = 44100

#criacao da figura MATPLOTLIB e dois eixos matplotlib
fig, (ax, ax2) = plt.subplots(2, figsize=(10,8))

#instancia da classe pyaudio
p = pyaudio.PyAudio()

#captura de dados do microfone
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

#variaveis para plotar
x = np.arange(0, 2 * CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

#objeto com dados aleatórios
line, = ax.plot(x, np.random.randn(CHUNK), '-', lw=2)

#line_fft, = ax2.semilogx(x_fft, np.random.randn(CHUNK), '-', lw=2)
line_fft, = ax2.plot(x_fft, np.random.randn(CHUNK), '-', lw=2)

#formatacao dos eixos
ax.set_title('Ondas Sonoras')
ax.set_ylim(0, 255)
ax.set_xlim(0, CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0,128,255])

ax2.set_title('Espectro')
ax2.set_ylim(0, 0.85)
ax2.set_xlim(0, 1600)
#plt.setp(ax2, xticks=[500, 1000, 2000, 3000, 4000])
#ax2.set_xlim(20, RATE/2)


plt.show(block=False)
note = ''
previous_note = '1'
time_start = 0


#------------------- DECLARAÇÃO DE VARIÁVEIS -------------------#

#-------------------     LOOP PRINCIPAL      -------------------#

while True:
    #dados binarios
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

    while i < len(splitedY):
        if splitedY[i] > maxY:
            maxY = splitedY[i]
            maxX = i
        i = i + 1

    #--- PRINTA O PICO DO ESPECTRO ---#

    #plt.plot(splitedX[maxX], maxY, '*', lw=1)
    #ax2.plot(splitedX[maxX], maxY, 'ro', lw=1)
    #ax2.annotate('*', xy=(splitedX[maxX], maxY))

    #--- IMPRIME O NOME E O SÍMBOLO DA NOTA TOCADA ---#
    note = rules.define_note(splitedX[maxX])

    if(note == previous_note):
        #print(note + ' ' + previous_note)
        pass
    else:
        time_elapsed = time.time()
        total_time = time_elapsed - time_start
        if(total_time > 0.19):
            note_symbol = rules.note_figure(float(total_time))
            print(note, time_elapsed - time_start)
            print(note_symbol)
        time_start = time_elapsed

    previous_note = note


    #atualiza figura
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
    except TclError:
        break

#-------------------     LOOP PRINCIPAL      -------------------#
