import pyaudio
import wave
import matplotlib.pyplot as plt

# the file name output you want to record into
filename = "recorded.wav"
# set the chunk size of 1024 samples
CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second
record_seconds = 5
# initialize PyAudio object
p = pyaudio.PyAudio()
# open stream object as input & output
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)
frames = []
print("Recording...")
for i in range(int(RATE / CHUNK * record_seconds)):
    data = stream.read(CHUNK)
    # if you want to hear your voice while recording
    #stream.write(data)
    frames.append(data)
print("Finished recording.")
# stop and close stream
stream.stop_stream()
stream.close()

# terminate pyaudio object
p.terminate()
# save audio file
# open the file in 'write bytes' mode
wf = wave.open(filename, "wb")
# set the channels
wf.setnchannels(CHANNELS)
# set the sample format
wf.setsampwidth(p.get_sample_size(FORMAT))
# set the sample rate
wf.setframerate(RATE)
# write the frames as bytes
wf.writeframes(b"".join(frames))
# close the file
wf.close()