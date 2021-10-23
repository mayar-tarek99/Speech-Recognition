import record
import process
import soundFile
from scipy.io import wavfile

# class Main(record.Recording , process.Processing):
#     def __init__(self,data,samplingFrequency,duration):
#         super().__init__(data, samplingFrequency , duration)
#         pass
        


def main():
    # samplerate, data = wavfile.read('./soundFiles/output.wav')

    p = record.Recording(None,44100,5)
    data = p.record()
    p.play()
    p.save()


main()