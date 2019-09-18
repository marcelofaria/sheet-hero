import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.randn(CHUNK))
ax.set_ylim(-255, 255)
ax.set_xlim(0, 4000)

while True:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2]
    line.set_ydata(data_int)
    print(line.get_xdata())
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()
