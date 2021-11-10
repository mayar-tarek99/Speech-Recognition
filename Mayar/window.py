import librosa
import numpy as np
from scipy.io import wavfile

# data = np.arange(0, 128)
samplerate, data = wavfile.read('./soundFiles/output.wav')
duration=librosa.get_duration(filename='./soundFiles/output.wav')
frame_len, hop_len = 16, 8
frames = librosa.util.frame(data, frame_length=frame_len, hop_length=hop_len)
windowed_frames = np.hanning(frame_len).reshape(-1, 1)*frames

# Print frames
for i, frame in enumerate(frames):
    print("Frame {}: {}".format(i, frame))

# Print windowed frames
for i, frame in enumerate(windowed_frames):
    print("Win Frame {}: {}".format(i, np.round(frame, 3)))