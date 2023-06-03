from librosa import load
from numpy.fft import fft, fftfreq
from numpy import abs, argmax

class note_detection:
    def __init__(self):
        self.__audio, self.__sample_rate = self.readfile()
    
    def readfile(self):
        
        """***
        This function used to load audio ".wav" file and convert it into array.
        return: audio, sample_rate
        
        ***"""
        audio_file = r'sample2.wav'
        audio, sample_rate = load(audio_file, sr=None)
        return audio, sample_rate
    

    
    def get_frequency(self):

        """
        Analyse a signal to achive the dominant frequency of the signal 
        return domaminant_frequency
        """    

        ffted = fft(self.__audio)
        magnitude = abs(ffted)
        frequency = fftfreq(len(magnitude), 1 / self.__sample_rate)
        
        # Find the dominant frequency
        dominant_frequency = round(frequency[argmax(magnitude)], 2)
        return dominant_frequency
   
    def tunning(self, note):
        """
        Calculate the difference in pitch between the true string and the correct string
        return differece
        """
        dominant_frequency = self.get_frequency()
        return (dominant_frequency - note)
        
          
        