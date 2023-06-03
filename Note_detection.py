import librosa
import numpy as np

class Note_detection:

    def readfile():
        
        """***
        This function used to load audio ".wav" file and convert it into array.
        return: audio, sample_rate
        
        ***"""
        audio_file = r'sample2.wav'
        audio, sample_rate = librosa.load(audio_file, sr=None)
        return audio, sample_rate
    

    
    def get_frequency():

        """
        Analyse a signal to achive the dominant frequency of the signal 
        return domaminant_frequency
        """    

        audio, sample_rate = Note_detection.readfile()
        fft = np.fft.fft(audio)
        magnitude = np.abs(fft)
        frequency = np.fft.fftfreq(len(magnitude), 1 / sample_rate)
        
        # Find the dominant frequency
        dominant_frequency = round(frequency[np.argmax(magnitude)], 2)
        return dominant_frequency
   
    def tunning(note):
        """
        Calculate the difference in pitch between the true string and the correct string
        return differece
        """
        dominant_frequency = Note_detection.get_frequency()
        return (dominant_frequency - note)
        
          
        