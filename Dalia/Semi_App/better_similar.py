from re import M
from cv2 import norm
from numpy.lib import arraypad
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
from scipy.ndimage.morphology import distance_transform_bf
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import librosa
import librosa.display
from scipy.stats.stats import pearsonr
from dtaidistance import dtw_ndim
from scipy.spatial.distance import pdist, squareform
y_in, sr_in = librosa.load("./Zeyad2.wav")
hop_length1= int(0.025*sr_in)
n_fft1=int(2*sr_in*0.0232)

print(sr_in)
mfcc_input = librosa.feature.mfcc(y=y_in, sr=sr_in,norm='ortho',hop_length=hop_length1,n_fft=n_fft1)
x_seq=mfcc_input.T
from scipy.stats import spearmanr

my_list=[]
my_x=[]
my_y=[]
DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav Aisha.wav aya.wav ibrahim.wav eisa.wav gehad.wav hisham.wav khaled.wav mohamed.wav samy.wav yehia.wav khloud.wav farouq.wav fatma.wav'.split()
for base in DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            #print("Audio Sampling Frequency",sr)
            hop_length= int(0.025*sr) #  ~510   HopLength
            n_fft=int(2*sr*0.0232)    #  ~1024  FrameSize
            mfcc = librosa.feature.mfcc(y=y, sr=sr,norm='ortho',hop_length=hop_length,n_fft=n_fft)
            D, wp = librosa.sequence.dtw(mfcc_input, mfcc,metric='cosine')
            x_seq=mfcc_input.T
            y_seq=mfcc.T
            N = y_seq.shape[0]
            M = x_seq.shape[0]
            distance = D[-1,-1]/(M+N)
            my_list.append(distance)
            zip_iterator = zip(DataBase, my_list)
            dictionary = dict(zip_iterator)
            similar = min(dictionary, key=dictionary.get)
print(dictionary)
print("most similar",similar)
            



