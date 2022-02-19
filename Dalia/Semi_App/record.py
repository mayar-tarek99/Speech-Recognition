# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 2

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)

# Record audio for the given number of seconds
print("start recording")
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("myhisham.wav", freq, recording)

# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)





# ////////////////////////Speech to text  ////////////////////////////////

# import speech_recognition as sr
# import arabic_reshaper
# from bidi.algorithm import get_display
# #print(sr.__version__)
# r = sr.Recognizer()
# import record


# harvard = sr.AudioFile('./DataBase/Yasmin.wav')
# with harvard as source:
#  r.adjust_for_ambient_noise(source,duration=0.03) #for noise
#  audio = r.record(source)
#  x= r.recognize_google(audio,language="en-US")
# #  reshaped_text1 = arabic_reshaper.reshape(x)    # correct its shape
# #  bidi_text1 = get_display(reshaped_text1)           # correct its direction
#  print(x)