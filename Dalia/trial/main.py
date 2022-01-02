import record
import process
import soundFile
from scipy.io import wavfile
import speech_to_text
import plotAudio
import Data_Base_spectogram
import search_text 

# class Main(record.Recording , process.Processing):
#     def __init__(self,data,samplingFrequency,duration):
#         super().__init__(data, samplingFrequency , duration)
#         pass
        


# def main():
#     # samplerate, data = wavfile.read('./soundFiles/output.wav')

#     # p = record.Recording(None,44100,5)
#     # data = p.record()
#     # p.play()
#     # p.save()

#     # #Conversion To text
#     # t= speech_to_text.To_Text("output.wav",44100,None)
#     # q= t.convert()
#     # print(q)

#     # # PlotAudio
#     # a = plotAudio.plotAudio("output.wav",44100,None)
#     # a.visualize("output.wav")

#     # Extract specto from dB
#     e =Data_Base_spectogram.Extract_specto_from_DB(None)
#     e.Spectogram()

#     # # search by text
#     # s=search_text.search_by_text("output.wav",44100,None)
#     # s.search_text(q)
    

# main()



import record , process
from scipy.io import wavfile

class Main(record.Recording , process.Processing):
    def _init_(self, data, samplingFrequency , duration):
        record.Recording._init_(self, data, samplingFrequency , duration)
        process.Processing._init_(self,data, samplingFrequency )
        pass
        


def main():
   
    p = Main(None, 44100,5)
    mydata = p.record()
    p.save()
    mydata2 = mydata.flatten()

    # samplerate, data = wavfile.read('./soundFiles/output.wav')
    l = Main(mydata2, 44100,5)
   # l.extractFeatures()
   # l.Hash()
    l.play()
    l.save()



main()