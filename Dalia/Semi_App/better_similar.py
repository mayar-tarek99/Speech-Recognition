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
import numpy
import scipy

y_in, sr_in = librosa.load("./db_matched_correctly/daiia.wav")
hop_length1= int(0.015*sr_in)
# hop_length1= 256
n_fft1=int(2*sr_in*0.0232)

print(sr_in)
mfcc_input = librosa.feature.mfcc(y=y_in, sr=sr_in,norm='ortho',hop_length=hop_length1,n_fft=n_fft1,n_mfcc=10)
# mfcc_input = librosa.feature.chroma_cens(y_in, sr=sr_in, hop_length=hop_length1)
x_seq=mfcc_input.T
from scipy.stats import spearmanr

my_list=[]
my_x=[]
my_y=[]
DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav Aisha.wav aya.wav ibrahim.wav eisa.wav gehad.wav hisham.wav khaled.wav mohamed.wav samy.wav yehia.wav khloud.wav farouq.wav fatma.wav'.split()
for base in DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            #print("Audio Sampling Frequency",sr)
            hop_length= int(0.015*sr) #  ~510   HopLength
            hop_length= 256
            n_fft=int(2*sr*0.0232)    #  ~1024  FrameSize
            mfcc = librosa.feature.mfcc(y=y, sr=sr,norm='ortho',hop_length=hop_length,n_fft=n_fft,n_mfcc=10)
            # mfcc = librosa.feature.chroma_cens(y, sr=sr, hop_length=hop_length)
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
            grade = min(my_list)
print(dictionary)
print("most similar",similar,grade)
            





# def dtw_table(x, y, distance=None):
#     if distance is None:
#         distance = scipy.spatial.distance.euclidean
#     nx = len(x)
#     ny = len(y)
#     table = numpy.zeros((nx+1, ny+1))
    
#     # Compute left column separately, i.e. j=0.
#     table[1:, 0] = numpy.inf
        
#     # Compute top row separately, i.e. i=0.
#     table[0, 1:] = numpy.inf
        
#     # Fill in the rest.
#     for i in range(1, nx+1):
#         for j in range(1, ny+1):
#             d = distance(x[i-1], y[j-1])
#             table[i, j] = d + min(table[i-1, j], table[i, j-1], table[i-1, j-1])
#     return table

# def dtw(x, y, table):
#     i = len(x)
#     j = len(y)
#     path = [(i, j)]
#     while i > 0 or j > 0:
#         minval = numpy.inf
#         if table[i-1][j-1] < minval:
#             minval = table[i-1, j-1]
#             step = (i-1, j-1)
#         if table[i-1, j] < minval:
#             minval = table[i-1, j]
#             step = (i-1, j)
#         if table[i][j-1] < minval:
#             minval = table[i, j-1]
#             step = (i, j-1)
#         path.insert(0, step)
#         i, j = step
#     return numpy.array(path)


# D = dtw_table(mfcc.T, mfcc_input.T, distance=scipy.spatial.distance.cosine)
# path = dtw(mfcc.T, mfcc_input.T, D)

# print(D)
# print(path)