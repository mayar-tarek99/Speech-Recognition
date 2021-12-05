from matplotlib.colors import BoundaryNorm
import librosa
import librosa.display
import numpy
import scipy.io.wavfile
from scipy.fftpack import dct
import matplotlib.pyplot as plt
import numpy as np


#Step 1 - read the audio and draw the time domain graph (sampling rate amplitude)
sample_rate, signal = scipy.io.wavfile.read('./DataBase/108.wav') # File assumed to be in the same directory
signal = signal[0:int(3.5 * sample_rate)]
# plot the wave
time = np.arange(0,len(signal))*(1.0 / sample_rate)
# plt.plot(time,signal)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Signal in the Time Domain ")
PLT. Grid ('on ') scale, on: Yes, off: No.


#Step 2 - pre emphasis
#Eliminate high frequency signals. Because high frequency signals are often similar,
#By subtracting the time before and after, the high-frequency signal can be almost erased, leaving the low-frequency signal.
#Principle: Y (T) = x (T) − α x (t − 1)

pre_emphasis = 0.97
emphasized_signal = numpy.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])


time = np.arange(0,len(emphasized_signal))*(1.0 / sample_rate)
# plt.plot(time,emphasized_signal)
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Signal in the Time Domain after Pre-Emphasis")
# PLT. Grid ('on ') scale, on: Yes, off: No.


#Step 3: take the frame and express it with the frame
Frame size = 0.025 frame length
Frame × strip = 0.01 × step

#Frame length - the number of samples corresponding to one frame, frame step - the number of samples corresponding to one step
frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate # Convert from seconds to samples
Signal? Length = length (highlighted? Signal)? Total number of samples

frame_length = int(round(frame_length))
frame_step = int(round(frame_step))

Total frame number
num_frames = int(numpy.ceil(float(numpy.abs(signal_length - frame_length)) / frame_step)) # Make sure that we have at least 1 frame

pad_signal_length = num_frames * frame_step + frame_length
z = numpy.zeros((pad_signal_length - signal_length))
pad_signal = numpy.append(emphasized_signal, z) # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal

# Construct an array by repeating A（200） the number of times given by reps（348）.
#This is a wonderful way of writing. Purpose: use matrix to express the number of frames, 348 * 200348 - the total number of frames, 200 - the number of samples per frame
#The first frame is 0, 1, 2... 200; the second frame is 80, 81, 81... 280, and so on
indices = numpy.tile(numpy.arange(0, frame_length), (num_frames, 1)) + numpy.tile(numpy.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
frames = pad_signal[indices.astype(numpy.int32, copy=False)] # Copy of the array indices
#Frame: 348 * 200, abscissa 348 is the number of frames, i.e. time; ordinate 200 is the 200 millisecond time of a frame, and the internal value represents the signal amplitude

# plt.matshow(frames, cmap='hot')
# plt.colorbar()
# plt.figure()
# plt.pcolormesh(frames)


#Step 4: add Hanming window
#The front and back endpoints of the default operation of Fourier transform are continuous, that is, the whole time period is just one cycle,
#However, the display is not so. So when this happens and FFT is still used,
#The single frequency periodic signal will be regarded as the superposition of multiple different frequency signals, rather than the original frequency, which leads to the problem of spectrum leakage

Frames * = numpy.hamming (frame ﹐ length) ﹐ multiplication, similar to convolution
# # frames *= 0.54 - 0.46 * numpy.cos((2 * numpy.pi * n) / (frame_length - 1)) # Explicit Implementation **

# plt.pcolormesh(frames)


#Step 5 - Fourier transform spectrum and energy spectrum

#Expand 348 * 200 to 348 * 512
NFFT = 512
mag_frames = numpy.absolute(numpy.fft.rfft(frames, NFFT)) # Magnitude of the FFT
pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2)) # Power Spectrum


# plt.pcolormesh(mag_frames)
#
# plt.pcolormesh(pow_frames)


#Step 6, filter banks
#Formula: M = 2595 * log10 (1 + F / 700); F = 700 (10 ^ (M / 2595) - 1)
Nfilt = 40 × number of windows
low_freq_mel = 0
high_freq_mel = (2595 * numpy.log10(1 + (sample_rate / 2) / 700)) # Convert Hz to Mel
mel_points = numpy.linspace(low_freq_mel, high_freq_mel, nfilt + 2) # Equally spaced in Mel scale
hz_points = (700 * (10**(mel_points / 2595) - 1)) # Convert Mel to Hz
bin = numpy.floor((NFFT + 1) * hz_points / sample_rate)

fbank = numpy.zeros((nfilt, int(numpy.floor(NFFT / 2 + 1))))
for m in range(1, nfilt + 1):
 f_m_minus = int(bin[m - 1]) # left
 f_m = int(bin[m])  # center
 f_m_plus = int(bin[m + 1]) # right

 for k in range(f_m_minus, f_m):
 fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
 for k in range(f_m, f_m_plus):
 fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
filter_banks = numpy.dot(pow_frames, fbank.T)
filter_banks = numpy.where(filter_banks == 0, numpy.finfo(float).eps, filter_banks) # Numerical Stability
filter_banks = 20 * numpy.log10(filter_banks) # dB;348*26

# plt.subplot(111)
# plt.pcolormesh(filter_banks.T)
# plt.grid('on')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()


#
#Step 7: Mel spectrum cepstrum coefficient MFCCs
Num? CEPS = 12? Take 12 coefficients
CEP? Lifter = 22? Cepstrum number??
mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1 : (num_ceps + 1)] # Keep 2-13
(nframes, ncoeff) = mfcc.shape
n = numpy.arange(ncoeff)
lift = 1 + (cep_lifter / 2) * numpy.sin(numpy.pi * n / cep_lifter)
mfcc *= lift #*

# plt.pcolormesh(mfcc.T)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')


#Step 8: average optimization
# to balance the spectrum and improve the Signal-to-Noise (SNR), we can simply subtract the mean of each coefficient from all frames.

filter_banks -= (numpy.mean(filter_banks, axis=0) + 1e-8)
mfcc -= (numpy.mean(mfcc, axis=0) + 1e-8)

# plt.subplot(111)
# plt.pcolormesh(mfcc.T)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()


#Direct spectrum analysis
# plot the wave
# plt.specgram(signal,Fs = sample_rate, scale_by_freq = True, sides = 'default')
# plt.ylabel('Frequency(Hz)')
# plt.xlabel('Time(s)')
# plt.show()



plt.figure(figsize=(10, 4))
mfccs = librosa.feature.melspectrogram(signal,sr=8000,n_fft=512,n_mels=40)
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()