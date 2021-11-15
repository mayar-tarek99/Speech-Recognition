import sounddevice as sd

class SoundFile:
    def __init__(self, data , samplingFrequency, **kwargs):
        self.data = data 
        self.samplingFrequency = samplingFrequency
 
    def play(self):
        sd.play(self.data, self.samplingFrequency)
        sd.wait()
        print ("Play Audio Complete")