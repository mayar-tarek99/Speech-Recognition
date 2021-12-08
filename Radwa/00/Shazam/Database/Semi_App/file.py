#########################
########################## 
# Reacord DataBase Audio
#########################
##########################
# Import the required module for text 
# to speech conversion
from gtts import gTTS
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
  
# This module is imported so that we can 
# play the converted audio
# import os
  
# # The text that you want to convert to audio
# mytext = 'Salah'
  
# # Language in which you want to convert
# language = 'ar'
  
# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
  
# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("Salah.mp3")
  
# Playing the converted file
# os.system("start  welcome.mp3")

#############################################################################################################
#############################################################################################################



#########################
########################## 
# Extracting Features From These AUDIOS:::
#########################
##########################


def Spectogram():
        header = 'filename spectral_centroid spectral_rolloff mfcc chroma_stft'.split()
        file = open('dataset.csv', 'w', newline='')
        with file:
          writer = csv.writer(file)
          writer.writerow(header)
        cmap = plt.get_cmap('inferno')
        plt.figure(figsize=(8,8))
        DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav '.split()
        for base in DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            print("Audio Sampling Frequency",sr)
            plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
            plt.axis('off')
            plt.savefig(f'img_data/{base[:-3].replace(".", "")}.png') 
             # plt.clf()           
            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
            to_append = f'{DataBase.index(base)} {str(imagehash.phash(Image.fromarray(spec_cent)))} {str(imagehash.phash(Image.fromarray(rolloff)))} {str(imagehash.phash(Image.fromarray(chroma_stft)))} {str(imagehash.phash(Image.fromarray(mfcc)))}'    
            file = open('dataset.csv', 'a', newline='')
            with file:
               writer = csv.writer(file)
               writer.writerow(to_append.split())
            #    return mfcc
Spectogram()