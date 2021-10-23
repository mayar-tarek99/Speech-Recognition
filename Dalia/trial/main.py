import record
import process
import soundFile
from scipy.io import wavfile
import speech_to_text
import plotAudio
import Data_Base_spectogram
# class Main(record.Recording , process.Processing):
#     def __init__(self,data,samplingFrequency,duration):
#         super().__init__(data, samplingFrequency , duration)
#         pass
        


def main():
    # samplerate, data = wavfile.read('./soundFiles/output.wav')

    p = record.Recording(None,44100,5)
    data = p.record()
    p.play()
    # p.save()
    
    #Conversion To text
    t= speech_to_text.To_Text("./DataBase/108.wav",44100,None)
    t.convert()
    # PlotAudio
    a = plotAudio.plotAudio("./DataBase/108.wav",44100,None)
    a.visualize("./DataBase/108.wav")
    # Extract specto from dB
    e =Data_Base_spectogram.Extract_specto_from_DB(None)
    e.Spectogram()

main()