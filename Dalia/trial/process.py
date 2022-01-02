import numpy as np
import librosa
import imagehash
from PIL import Image
import soundFile
from scipy.io import wavfile
from dtw import dtw



class Processing(soundFile.SoundFile):
    def __init__(self, data , samplingFrequency):
        super().__init__(data, samplingFrequency)
        self.spectrogram = None 
        self.centroid_feature = None
        self.rolloff_feature = None
        self.mfcc_feature = None
        self.chroma_stft_feature = None
        self.features_hashes=[]

    def extractSpectrogram(self):
        print ("spectrogram")
        try:
            self.spectrogram= librosa.amplitude_to_db(np.abs(librosa.stft(self.data)), ref=np.max)
        except:
            print("enter data")

    def extractFeatures(self):
        print ("extractFeatures")
        try:
            self.centroid_feature= librosa.feature.spectral_centroid(self.data, self.samplingFrequency)
            self.rolloff_feature= librosa.feature.spectral_rolloff(self.data, self.samplingFrequency)
            self.mfcc_feature = librosa.feature.mfcc(self.data, self.samplingFrequency)
            self.chroma_stft_feature = librosa.feature.chroma_stft(self.data, self.samplingFrequency) 
        except:
            print("enter data")
    

    def Hash(self):
        print ("Hash")
        try:
            features=[self.centroid_feature,self.rolloff_feature, self.mfcc_feature,self.chroma_stft_feature]
            for feature in features:
                self.features_hashes.append(list(str((imagehash.phash(Image.fromarray(feature))))))
            print(self.features_hashes)
            return self.features_hashes
        except:
            print("get features first!")


    

# samplerate, data = wavfile.read('./soundFiles/output.wav')
# p = Processing(data,samplerate)
# p.extractSpectrogram()
# p.extractFeatures()
# p.Hash()
