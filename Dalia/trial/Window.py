import librosa
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

# data = np.arange(0, 128)
FRAME_SIZE = 1024
HOP_LENGTH = 512
samplerate, data = wavfile.read('output.wav')
duration=librosa.get_duration(filename='output.wav')

frame_len, hop_len = 16,8
frames = librosa.util.frame(data, frame_length=frame_len, hop_length=hop_len)
windowed_frames = np.hanning(frame_len).reshape(-1, 1)*frames

# Print frames
for i, frame in enumerate(frames):
    print("Frame {}: {}".format(i, frame))

# Print windowed frames
rms_container =0
zcr_container=0
for i, frame in enumerate(windowed_frames):
    print("Win Frame {}: {}".format(i, np.round(frame, 3)))
    # Root-mean-squared energy with Librosa
    rms_audio = librosa.feature.rms(frame)[0]
    zcr_audio = librosa.feature.zero_crossing_rate(frame)[0]
    rms_container+=rms_audio
    zcr_container+=zcr_audio






framesLen = range(len(rms_audio))
t_rms = librosa.frames_to_time(framesLen, hop_length=hop_len)
t_zcr = librosa.frames_to_time(framesLen, hop_length=hop_len)
# print(zcr_audio.shape)
# print(rms_audio.shape)

# rms energy is graphed in red
def figPlot(color,type,title,t):

  plt.figure(figsize=(15, 17))
  ax = plt.subplot(3, 1, 1)
  librosa.display.waveplot(rms_audio, alpha=0.5)
  plt.plot(t,type , color=color)
  plt.ylim((-1, 1))
  plt.title(title)
  plt.show()

figPlot('r',rms_container,"AudioEnergy",t_rms)
figPlot('y',zcr_container,"Audio zero Crossing",t_zcr)
