import numpy as np
import librosa
import librosa.display
from librosa.core import load
import hashlib
from pydub import AudioSegment
import tempfile
from PIL import Image
import imagehash
import pylab
import os
import soundfile as sf
import pyquran as q
import arabic_reshaper
from difflib import SequenceMatcher


class audio():
    def __init__(self, Path: str):
        self.path = Path
        audioData = AudioSegment.from_mp3(self.path)[0:60000]
        wavdata = tempfile.mktemp('.wav')
        audioData.export(wavdata, format="wav")
        #print('&&&&&&&&&&&&&', audioData)
        self.data, self.fs = librosa.load(wavdata)
        #print('$$$$$$$$$$$$$$$$$$$$', self.data)
        #print('@@@@@@@@@@@@@@', self.fs)

    def loaddata(self):
        return self.data

    def loadfs(self):
        return self.fs

    def spectro(self):
        self.stft = np.abs(librosa.stft(self.data))
        self.spectro = librosa.amplitude_to_db(self.stft)
        librosa.display.specshow(self.spectro, y_axis='linear')
        pylab.savefig('spectros/spec.' + os.path.splitext(os.path.basename(self.path))
                      [0] + '.png', bbox_inches=None, pad_inches=0)
        pylab.close()

    def getSongName(self):
        baseFileName = os.path.basename(self.path)
        songName = os.path.splitext(baseFileName)[0]
        return songName

    def hashdata(self, datatohash):
        self.newimage = Image.fromarray(datatohash)
        self.hashed = imagehash.phash(self.newimage, hash_size=16)
        return self.hashed

    def feature1(self):
        self.melSpectrogram = librosa.feature.melspectrogram(
            y=self.data, sr=self.fs)
        self.hashedmelspec = self.hashdata(self.melSpectrogram)
        return self.hashedmelspec

    def feature2(self):
        self.chroma = librosa.feature.chroma_stft(y=self.data, sr=self.fs)
        self.hashedchroma = self.hashdata(self.chroma)
        return self.hashedchroma

    def feature3(self):
        self.mcff = librosa.feature.mfcc(y=self.data, sr=self.fs, n_mfcc=13)
        self.hashedmcff = self.hashdata(self.mcff)
        return self.hashedmcff

    def feature4(self):
        self.spectralcent = librosa.feature.spectral_centroid(
            y=self.data, sr=self.fs)
        self.hashedspectral = self.hashdata(self.spectralcent)
        return self.hashedspectral

    def feature5(self):
        self.rolloffFreq = librosa.feature.spectral_rolloff(
            y=self.data, sr=self.fs)[0]
        self.hashedrollof = self.hashdata(self.rolloffFreq)
        return self.hashedrollof

    def findsimilarto(self):
        self.results = []
        self.diffValue = [0, 0, 0, 0]
        audio1 = audio(
            './DataBase/vocals/بسم الله الرحمن الرحيم .. صوت (128  kbps) (shabakngy.com).mp3_vocals.mp3')
        audio2 = audio(
            './DataBase/vocals/بسم الله الرحمن الرحيم صوت جميل (192 kbps).mp3_vocals.mp3')
        oldFeats = [0, audio1.feature1(), audio1.feature2(), audio1.feature3()]
        newFeats = [0, audio2.feature1(), audio2.feature2(), audio2.feature3()]
        for j in range(1, 4):
            self.diffValue[j] = (1-(imagehash.hex_to_hash(str(oldFeats[j])) -
                                    imagehash.hex_to_hash(str(newFeats[j]))) / 256.0)
        print('NEW FEAT', oldFeats)
        print('SONG FEAT', newFeats)
        similarity = (self.diffValue[1] +
                      self.diffValue[2]+self.diffValue[3])/0.03
        print(similarity)


audio('./welcome.mp3').findsimilarto()


# aya = q.quran.get_verse(sura_number=1, verse_number=2)
# sora = q.quran.get_sura(108, with_tashkeel=False)
# #sora1 = q.quran.get_sura(108, with_tashkeel=False)
# sora1 = ['إن أعطيناك الكوثر', 'فصل لربك وانحر', 'إن شانئك هو الأبتر']
# print(sora, '-------', sora1)
# rev_sora = []
# for i in range(len(sora)):
#     reshaped_text = arabic_reshaper.reshape(sora[i])
#     rev_sora.append(reshaped_text[::-1])
# reshaped_text = arabic_reshaper.reshape(aya)
# rev_text = reshaped_text[::-1]  # slice backwards
# rev_sora.reverse()
# print(rev_sora)
# print(SequenceMatcher(None, sora, sora1).ratio())
