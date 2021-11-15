import record , process
from scipy.io import wavfile

class Main(record.Recording , process.Processing):
    def __init__(self, data, samplingFrequency , duration):
        record.Recording.__init__(self, data, samplingFrequency , duration)
        process.Processing.__init__(self,data, samplingFrequency )
        pass
        


def main():
   
    p = Main(None, 44100,5)
    mydata = p.record()
    p.save()
    mydata2 = mydata.flatten()

    # samplerate, data = wavfile.read('./soundFiles/output.wav')
    l = Main(mydata2, 44100,5)
    l.extractFeatures()
    l.Hash()
    l.play()
    l.save()



main()