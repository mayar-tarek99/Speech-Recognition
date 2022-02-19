import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd


# audio_file = './DataBase/Sara.wav'
audio_file2 = 'saya.wav'

# ipd.Audio(audio_file)
# audio,sr =librosa.load(audio_file)
audio2,sr2=librosa.load(audio_file2)
#print(sr)

# Root-mean-squared energy with Librosa
FRAME_SIZE = 1024
HOP_LENGTH = 512
# rms_audio = librosa.feature.rms(audio2, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
#print("SSSRRR",sr)

#print("f",frames)  #3ndy km frames 3la 7sb el duration btzeed
#print("t",t)  # first value is 0.02321995 which is 1024/44100
#print("rms",rms_audio.shape)





#ZCR
zcr_audio2 = librosa.feature.zero_crossing_rate(audio2, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
print("zcr",zcr_audio2)
# zcr_audio2 = librosa.feature.zero_crossing_rate(audio2, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]
# print("result",(zcr_audio2)
frames = range(len(zcr_audio2))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
print("time",t)
plt.plot(t, zcr_audio2, color="b")
plt.ylim(0, 1)
plt.show()


# def figPlot():

#   plt.figure(figsize=(15, 17))
#   ax = plt.subplot(3, 1, 1)
#   librosa.display.waveplot(audio2, alpha=0.5)
#   plt.plot(t, rms_audio, color="r")
#   plt.title("Audio Energy")
#   ax = plt.subplot(3, 1, 2)
#   plt.plot(t, zcr_audio2, color="b")
#   # plt.ylim((-1, 1))
#   plt.title("Zero crossing")
#   plt.show()
# figPlot()
# plt.figure(figsize=(15, 10))
# plt.plot(t, zcr_audio2, color="b")
# plt.ylim(0, 1)
# plt.show()
###########################################################################################################
# def spectogram():
#   chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr*2,hop_length=HOP_LENGTH,window="hann",n_fft=FRAME_SIZE)
#   mfcc = librosa.feature.mfcc(y=audio, sr=sr*2,hop_length=HOP_LENGTH,window="hann",n_fft=FRAME_SIZE)
#   rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr*2,hop_length=HOP_LENGTH,window="hann",n_fft=FRAME_SIZE)
#   spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr*2,hop_length=HOP_LENGTH,window="hann",n_fft=FRAME_SIZE)
  
#   fig, ax = plt.subplots(nrows=4, sharex=True, sharey=True)
#   img1 = librosa.display.specshow(mfcc, x_axis='time', ax=ax[0],sr=sr*2)
#   ax[0].set(title='MFCC')
#   fig.colorbar(img1, ax=[ax[0]])
#   img2 = librosa.display.specshow(rolloff, x_axis='time', ax=ax[1],sr=sr*2)
#   ax[1].set(title='ROLLOFF')
#   fig.colorbar(img2, ax=[ax[1]])
#   img3 = librosa.display.specshow(chroma_stft, x_axis='time', ax=ax[2],sr=sr*2)
#   ax[2].set(title='CHROMA_STFT')
#   fig.colorbar(img3, ax=[ax[2]])
#   img4 = librosa.display.specshow(spec_cent, x_axis='time', ax=ax[3],sr=sr*2)
#   ax[3].set(title='SPEC_CENT')
#   fig.colorbar(img4, ax=[ax[3]])
#   plt.show()

# spectogram()




# # RMSE from scratch

# def rmse(signal, frame_size, hop_length):
#     rmse = []
    
#     # calculate rmse for each frame
#     for i in range(0, len(signal), hop_length): 
#         rmse_current_frame = np.sqrt(sum(signal[i:i+frame_size]**2) / frame_size)
#         rmse.append(rmse_current_frame)
#     return np.array(rmse)


# rmse(audio2,FRAME_SIZE,HOP_LENGTH)