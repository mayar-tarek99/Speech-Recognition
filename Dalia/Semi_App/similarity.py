from re import M
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
from scipy.ndimage.morphology import distance_transform_bf
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import librosa
import librosa.display


data1,sr1=librosa.load("./DataBase/hisham.wav")
data2,sr2=librosa.load("./DataBase/eisa.wav")
data3,sr3=librosa.load("./DataBase/Salah.wav")
data4,sr4=librosa.load("./DataBase/hisham.wav")
data5,sr5=librosa.load("./DataBase/Salah.wav")
data6,sr6=librosa.load("./myhassan.wav")

# distance,path =fastdtw(data1, data1)
# print("hisham,eisa",100-distance )

# distance,path =fastdtw(data1, data3)
# print("hisham,Hassan",100-distance )

# distance,path =fastdtw(data4, data5)
# print("sara,salah",100-distance )

# distance,path =fastdtw(data3, data6)
# print("hassan,hassan",distance )


# import numpy as np
# import matplotlib.pyplot as plt
# X = librosa.feature.mfcc(y=data3, sr=sr3)
# Y = librosa.feature.mfcc(y=data6, sr=sr6)
# x_seq=X.T
# y_seq=Y.T
# D, wp = librosa.sequence.dtw(X, Y, subseq=True)
# N=y_seq.shape[0]
# M=x_seq.shape[0]
# distance = D[-1,1]/(M+N)
# print(distance)
# fig, ax = plt.subplots(nrows=2, sharex=True)
# img = librosa.display.specshow(D, x_axis='frames', y_axis='frames',
#                                ax=ax[0])
# ax[0].set(title='DTW cost', xlabel='Noisy sequence', ylabel='Target')
# ax[0].plot(wp[:, 1], wp[:, 0], label='Optimal path', color='y')
# ax[0].legend()
# fig.colorbar(img, ax=ax[0])
# ax[1].plot(D[-1, :] / wp.shape[0])
# ax[1].set(xlim=[0, Y.shape[1]], ylim=[0, 2],
#           title='Matching cost function')
# # plt.show()
# print(D)
# print(wp)



# import matplotlib

# fig = plt.figure(figsize=(16, 8))
# # Plot x_1
# plt.subplot(2, 1, 1)
# librosa.display.waveplot(data3, sr=sr3)
# plt.title('Data1')
# ax1 = plt.gca()

# # Plot x_2
# plt.subplot(2, 1, 2)
# librosa.display.waveplot(data6, sr=sr6)
# plt.title('Data2')
# ax2 = plt.gca()

# plt.tight_layout()
# trans_figure = fig.transFigure.inverted()
# lines = []
# arrows = 30 
# #Returns num evenly spaced samples, calculated over the interval [start, stop].
# points_idx = np.int16(np.round(np.linspace(0, wp.shape[0] - 1, arrows)))

# # for tp1, tp2 in zip((wp[points_idx, 0]) * hop_size, (wp[points_idx, 1]) * hop_size):
# for tp1, tp2 in wp[points_idx] * 512 / sr1:
#     # get position on axis for a given index-pair
#     coord1 = trans_figure.transform(ax1.transData.transform([tp1, 0]))
#     coord2 = trans_figure.transform(ax2.transData.transform([tp2, 0]))
#     # draw a line
#     line = matplotlib.lines.Line2D((coord1[0], coord2[0]),
#                                    (coord1[1], coord2[1]),
#                                    transform=fig.transFigure,
#                                    color='red')
#     lines.append(line)

# fig.lines = lines
# plt.tight_layout()
# plt.show()















y_in, sr_in = librosa.load("./myahmed.wav")
mfcc_input = librosa.feature.mfcc(y=y_in, sr=sr_in)

my_list=[]
DataBase = 'Ahmed.wav Amira.wav Dalia.wav Hassan.wav Maram.wav Maryem.wav Mayar.wav Mostafa.wav Radwa.wav Raouf.wav Salah.wav Sara.wav Shady.wav Yasmin.wav Tarek.wav Zeyad.wav Aisha.wav aya.wav ibrahim.wav eisa.wav gehad.wav hisham.wav khaled.wav mohamed.wav samy.wav yehia.wav khloud.wav farouq.wav fatma.wav'.split()
for base in DataBase:
            y, sr = librosa.load("./DataBase/"+base, mono=True, duration=5)
            #print("Audio Sampling Frequency",sr)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            D, wp = librosa.sequence.dtw(mfcc_input, mfcc, subseq=True)
            x_seq=mfcc_input.T
            y_seq=mfcc.T
            N = y_seq.shape[0]
            M = x_seq.shape[0]
            distance = D[-1,-1]/(M+N)
            print("d",D)
            my_list.append(distance)
            zip_iterator = zip(DataBase, my_list)
            dictionary = dict(zip_iterator)
            similar = min(dictionary, key=dictionary.get)
print(dictionary)
print("most similar",similar)
            # similar = min(my_list, key=lambda x:abs(x-myNumber))
































