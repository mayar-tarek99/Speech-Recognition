import sounddevice as sd
from scipy.io.wavfile import write
import soundFile
import numpy as np

class Recording (soundFile.SoundFile):
    def __init__(self, data ,samplingFrequency , duration):
        super().__init__(data, samplingFrequency)
        self.duration = duration  # Duration of recording

    def record(self):
        self.data = sd.rec(int(self.duration * self.samplingFrequency), samplerate=self.samplingFrequency, channels=1,dtype=np.int16)
        print ("Recording Audio")
        sd.wait()  # Wait until recording is finished
        print ("Audio recording complete , Play Audio")
        return self.data
        
    def save(self):
        write('output.wav', self.samplingFrequency, self.data)  # Save as WAV file 
        print ("Audio Saved")

p = Recording(None,44100,5)
p.record()
p.play()
p.save()