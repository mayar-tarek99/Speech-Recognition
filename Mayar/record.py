import numpy as np 
import sounddevice as sd
from scipy.io.wavfile import write
import soundFile

class Recording (soundFile.SoundFile):
    def __init__(self , data ,samplingFrequency , duration):
        super().__init__(data , samplingFrequency)
        self.duration = duration  # Duration of recording

    def record(self):
        #channels=1,dtype=np.int16
        self.data = sd.rec(int(self.duration * self.samplingFrequency), samplerate=self.samplingFrequency, channels=1,dtype='float64')
        print ("Recording Audio")
        sd.wait()  # Wait until recording is finished
        print ("Audio recording complete , Play Audio")
        return self.data
        
    def save(self):
        write('./soundFiles/output.wav', self.samplingFrequency, self.data)  # Save as WAV file 
        print ("Audio Saved")