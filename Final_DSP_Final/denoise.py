#Write a program which can record and plot audio in real time

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

# constants

CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

# pyaudio class instance

p = pyaudio.PyAudio()

# stream object to get data from microphone

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# create matplotlib figure and axes

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(15, 15))

# variable for plotting

x = np.arange(0, 2 * CHUNK, 2)       # samples (waveform)
freq = (1/(0.01*CHUNK)) * np.arange(CHUNK)

# create a line object with random data

line, = ax1.plot(x, np.random.rand(CHUNK), '-', lw=2)

# create semilogx line for PSD

line_PSD, = ax2.plot(freq, np.random.rand(CHUNK))

# format waveform axes

ax1.set_title('AUDIO WAVEFORM')
ax1.set_ylim(0, 255)
ax1.set_xlim(0, 2 * CHUNK)
plt.setp(ax1, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

ax2.set_title('PSD')
ax2.set_ylim(0, 100000)

threshold = 15000

ax3.set_title('CLEAN WAVEFORM')
ax3.set_ylim(0, 255)
ax3.set_xlim(0, 2 * CHUNK)
ax2.axhline(threshold, ls= '--', c= 'r')
plt.setp(ax3, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

line_clean, = ax3.plot(x, np.random.rand(CHUNK), '-', lw=2)

# show axes

fig.show()

# for measuring frame rate

frame_count = 0
start_time = time.time()

while True:
    
        # binary data
    
        data = stream.read(CHUNK)
    
        # convert data to integers, make np array, then offset it by 127
    
        data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    
        data_np = np.array(data_int, dtype='b')[::2] + 128

        ffted = np.fft.fft(data_np)
        
        PSD = ffted * np.conj(ffted) / CHUNK
        
        line.set_ydata(data_np)

        # PSD
        line_PSD.set_ydata(PSD)

        ## Filter out noise
        
        psd_idxs = PSD > threshold #array of 0 and 1

        # psd_clean = PSD * psd_idxs #zero out all the unnecessary powers
        ffted_clean = psd_idxs * ffted #used to retrieve the signal

        # line_PSD.set_ydata(psd_clean)
        
        signal_filtered = np.fft.ifft(ffted_clean) #inverse fourier transform
        
        line_clean.set_ydata(signal_filtered)
        
        # update figure canvas
    
        try:
            fig.canvas.draw()
            fig.canvas.flush_events()
            frame_count += 1
    
        except TclError:
    
            # calculate average frame rate
    
            frame_rate = frame_count / (time.time() - start_time)
    
            print('stream stopped')
            print('average frame rate = {:.0f} FPS'.format(frame_rate))
            break
    
# close stream

stream.stop_stream()
stream.close()
p.terminate()
