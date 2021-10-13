from typing import FrozenSet
import sounddevice as sd
from scipy.io.wavfile import write

recording = sd.rec(int(3*44100),samplerate=44100,channels=2)
sd.wait()
sd.play(recording,44100)
sd.wait()
write('./output.wav',44100,recording)
