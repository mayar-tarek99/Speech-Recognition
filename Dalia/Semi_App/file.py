#########################
########################## 
# Reacord DataBase Audio
#########################
##########################
# Import the required module for text 
# to speech conversion

import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pathlib
# from sklearn.preprocessing import LabelEncoder, StandardScalerimport keras
from keras import layers
from keras import layers
import keras
import csv
import imagehash
from scipy.spatial import distance

# This module is imported so that we can 
# play the converted audio
# from gtts import gTTS  
# import os
  
# # # The text that you want to convert to audio
# mytext = 'kathem' 
# # # Language in which you want to convert
# language = 'ar'  
# # # Passing the text and language to the engine, 
# # # here we have marked slow=False. Which tells 
# # # the module that the converted audio should 
# # # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
  
# # # Saving the converted audio in a mp3 file named
# # # welcome 
# myobj.save("kathem.mp3")
  
# Playing the converted file
# os.system("start  welcome.mp3")
# from pydub import AudioSegment

# #files                                                                       
# src = "Aisha.mp3"
# dst = "Aisha.wav"

# # convert wav to mp3                                                            
# audSeg = AudioSegment.from_mp3("Aisha.mp3")
# audSeg.export(dst, format="wav")
#############################################################################################################
#############################################################################################################



#########################
########################## 
# Extracting Features From These AUDIOS:::
#########################
##########################
# FRAME_SIZE = 1024
# HOP_LENGTH = 512
# to_append =[[],[],[],[]]
# spec_cent=[]
# FRAME_SIZE = 1024
# HOP_LENGTH = 512
# def Spectogram():
#         header = 'filename spectral_centroid spectral_rolloff mfcc chroma_stft  '.split()
#         file = open('dataset.csv', 'w', newline='')
#         with file:
#           writer = csv.writer(file)
#           writer.writerow(header)
#         cmap = plt.get_cmap('inferno')
#         plt.figure(figsize=(8,8))
#         DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav Aisha.wav aya.wav ibrahim.wav eisa.wav gehad.wav hisham.wav khaled.wav mohamed.wav samy.wav yehia.wav khloud.wav farouq.wav fatma.wav'.split()
#         for base in DataBase:
#             y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
#             print("Audio Sampling Frequency",sr)
#             plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
#             plt.axis('off')
#             plt.savefig(f'img_data/{base[:-3].replace(".", "")}.png') 
#              # plt.clf()           
#             chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
#             mfcc = librosa.feature.mfcc(y=y, sr=sr)
#             rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
#             spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
#             spec_cent=spec_cent
#             zero = librosa.feature.zero_crossing_rate(y=y,frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)
#             lpc = librosa.lpc(y,16)
#             to_append = f'{DataBase.index(base)} {str(imagehash.phash(Image.fromarray(spec_cent)))} {str(imagehash.phash(Image.fromarray(rolloff)))} {str(imagehash.phash(Image.fromarray(mfcc)))} {str(imagehash.phash(Image.fromarray(chroma_stft)))}'    
#             file = open('dataset.csv', 'a', newline='')
#             to_append=to_append
#             with file:
#                writer = csv.writer(file)
#                writer.writerow(to_append.split())
#             #    return mfcc
# Spectogram()




























# features_hashes=[]
# def audio_input_features ():
#         """spectrogram [Makes the spectrogram of a song , calls a function to hash the the spectro. and a function to extract the features of the song]
#         """
#         audio,sr = librosa.load('daiia.wav')
        
#         #Song spectogram
#         #song_spectogram= librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
#         spectral_centroid_feature= librosa.feature.spectral_centroid(audio, sr=sr)
#         spectral_rolloff_feature= librosa.feature.spectral_rolloff(audio, sr=sr)
#         mfcc_feature = librosa.feature.mfcc(audio, sr=sr)#Mel-Frequency Cepstral Coefficients(MFCCs)
#         chroma_stft_feature = librosa.feature.chroma_stft(audio,sr=sr) #Chroma feature
#         features=[spectral_centroid_feature,spectral_rolloff_feature, mfcc_feature,chroma_stft_feature]
#         for feature in features:
#           features_hashes.append(list(str((imagehash.phash(Image.fromarray(feature))))))
#           #print(features_hashes)


# #audio_input_features()





# def Data_Base_Comparing():
#         Distancing_Hamming_reverse=[[],[],[],[]]
#         similarity_index=[]
#         for i in range(len(spec_cent)): 
#           for j in range(len(features_hashes)):
#               Distancing_Hamming_reverse[j].append(1-distance.hamming(to_append[j][i], features_hashes[j]))
#           similarity_index.append(100*((Distancing_Hamming_reverse[0][i]+Distancing_Hamming_reverse[1][i]+0.5*Distancing_Hamming_reverse[2][i]+0.5*Distancing_Hamming_reverse[3][i])/3)) 
#         print(similarity_index) 


# #Data_Base_Comparing()




















import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import pathlib
# from sklearn.preprocessing import LabelEncoder, StandardScalerimport keras
from keras import layers
from keras import layers
import keras
import csv
import imagehash
from scipy.spatial import distance
import librosa.display
import IPython.display as ipd

#########################
########################## 
# Extracting Features From These AUDIOS:::
#########################
##########################
FRAME_SIZE = 1024
HOP_LENGTH = 512
to_append =[[],[],[],[]]
spec_cent=[]
FRAME_SIZE = 1024
HOP_LENGTH = 512
def Spectogram():

        plt.figure(figsize=(8,8))
DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav Aisha.wav aya.wav ibrahim.wav eisa.wav gehad.wav hisham.wav khaled.wav mohamed.wav samy.wav yehia.wav khloud.wav farouq.wav fatma.wav'.split()        
for base in DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            print("Audio Sampling Frequency",sr)
#           plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
            mfcc = librosa.feature.mfcc(y=y, sr=sr,hop_length=HOP_LENGTH,n_fft=FRAME_SIZE)
            librosa.display.specshow(mfcc, x_axis='time',sr=sr)
            plt.axis('off')
            plt.savefig(f'img_data/{base[:-3].replace(".", "")}.png') 
             # plt.clf()           

Spectogram()