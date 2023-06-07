from numpy import log2, log10, floor, ceil, float32, zeros, cos, linspace, fromstring, int16, pi, fft
from pyaudio import PyAudio, paInt16
from time import time
from tkinter import TclError
from matplotlib import pyplot as plt

class recorder:
    def __init__(self):
        self.freq = 0
        
        self.difference = 0

        self.stop_record = False
        
        self.advanceMode = False
        
    def record(self, note):
        NOTE_MIN = 40
        NOTE_MAX = 71
        FSAMP = 22050
        FRAME_SIZE = 2048
        FRAMES_PER_FFT = 16

        SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
        FREQ_STEP = float(FSAMP) / SAMPLES_PER_FFT

        def freq_to_number(f):
            return 69 + 12 * log2(f / 440.0)

        def number_to_freq(n):
            return 440 * 2.0 ** ((n - 69) / 12.0)

        def note_to_fftbin(n):
            return number_to_freq(n) / FREQ_STEP

        imin = max(0, int(floor(note_to_fftbin(NOTE_MIN - 1))))
        imax = min(SAMPLES_PER_FFT, int(ceil(note_to_fftbin(NOTE_MAX + 1))))

        buf = zeros(SAMPLES_PER_FFT, dtype=float32)
        num_frames = 0

        stream = PyAudio().open(format=paInt16,
                                        channels=1,
                                        rate=FSAMP,
                                        input=True,
                                        frames_per_buffer=FRAME_SIZE)

        stream.start_stream()

        window = 0.5 * (1 - cos(linspace(0, 2*pi, SAMPLES_PER_FFT, False)))

        # print ('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')
        # print()
        
        fig, ax = plt.subplots(figsize=(15, 7))
        
        frame_count = 0
        start_time = time()
                
        while stream.is_active():
            buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
            buf[-FRAME_SIZE:] = fromstring(stream.read(FRAME_SIZE), int16)
            ffted = fft.rfft(buf * window)
            
            freq = (abs(ffted[imin:imax]).argmax() + imin) * FREQ_STEP
            
            num_frames += 1
            if num_frames >= FRAMES_PER_FFT:
                if not self.advanceMode:
                    self.freq =  freq
                    
                    self.difference = freq - note    
                else:
                    magnitude = abs(ffted)
                    magnitude_db = 20 * log10(magnitude)
                    
                    spectrum, = ax.plot(magnitude_db)                               
                    
                    try:
                        fig.canvas.draw()
                        fig.canvas.flush_events()
                        frame_count += 1
                        
                    except TclError:
                        
                        # calculate average frame rate
                        frame_rate = frame_count / (time() - start_time)
                        
                        print('stream stopped')
                        print('average frame rate = {:.0f} FPS'.format(frame_rate))
                        break
            
            if self.stop_record:
                print('stopped')
                return        
            

run = recorder()
run.advanceMode = True
run.record(110)