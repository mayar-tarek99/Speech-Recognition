import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()
import record

class To_Text(record.Recording):
    def __init__(self,data,samplingFrequency,duration):
        super().__init__(data,samplingFrequency,duration)
        self.Quran = sr.AudioFile(data)
    def convert(self):
        with self.Quran as source:
          audio = r.record(source)
          text= r.recognize_google(audio,language="ar-EG")
          print(text)





# harvard = sr.AudioFile('108.wav')
# with harvard as source:
#  audio = r.record(source)
#  x= r.recognize_google(audio,language="ar-EG")
#  print(x)
#  if "الكوثر" in x:
#      print("yees")
#  else:
#      print("NO")

# Quran2 = sr.AudioFile('jackhammer.wav')
# with Quran2 as source2:
# #  r.adjust_for_ambient_noise(source) //for noise
#  audio2 = r.record(source2)
#  x2= r.recognize_google(audio,language="ar-EG")
#  print(x2)
#  if  x[0:5]  == x2[0:5]:
#      print("yees")
#  else:
#      print("NO")















   


