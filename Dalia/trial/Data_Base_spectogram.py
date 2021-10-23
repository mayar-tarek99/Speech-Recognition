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


class Extract_specto_from_DB():
    def __init__(self,DataBase):
        self.database=DataBase
    def Spectogram(self):
        header = 'filename spectral_centroid spectral_rolloff mfcc chroma_stft'.split()
        file = open('dataset.csv', 'w', newline='')
        with file:
          writer = csv.writer(file)
          writer.writerow(header)
        cmap = plt.get_cmap('inferno')
        plt.figure(figsize=(8,8))
        self.DataBase = '108.wav 109.wav'.split()
        for base in self.DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
            plt.axis('off')
            plt.savefig(f'img_data/{base[:-3].replace(".", "")}.png') 
             # plt.clf()           
            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
            to_append = f'{self.DataBase.index(base)} {np.mean(spec_cent)} {np.mean(rolloff)} {np.mean(chroma_stft)} {np.mean(mfcc)}'    
            file = open('dataset.csv', 'a', newline='')
            with file:
               writer = csv.writer(file)
               writer.writerow(to_append.split())




        
       
        


       

