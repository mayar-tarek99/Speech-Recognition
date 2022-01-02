import speech_recognition as sr
import arabic_reshaper
from bidi.algorithm import get_display
print(sr.__version__)
r = sr.Recognizer()
import record

# class To_Text(record.Recording):
#     def __init__(self,data,samplingFrequency,duration):
#         super().__init__(data,samplingFrequency,duration)
#         self.Quran = sr.AudioFile(data)
#     def convert(self):
#         print("convert to text....")
#         with self.Quran as source:
#           r.adjust_for_ambient_noise(source)
#           audio = r.record(source)
#           text= r.recognize_google(audio,language="ar-EG")
#         #   reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
#         #   bidi_text = get_display(reshaped_text)           # correct its direction
#           return text





harvard = sr.AudioFile('Mostafa.wav')
with harvard as source:
 r.adjust_for_ambient_noise(source,duration=0.03) #for noise
 audio = r.record(source)
 x= r.recognize_google(audio,language="ar-EG")
 reshaped_text1 = arabic_reshaper.reshape(x)    # correct its shape
 bidi_text1 = get_display(reshaped_text1)           # correct its direction
 print(bidi_text1)
#  if "الكوثر" in x:
#      print("yees")
#  else:
#      print("NO")

Quran2 = sr.AudioFile('Mothtafa.wav')
with Quran2 as source2:
 r.adjust_for_ambient_noise(source2,duration=0.15) #for noise
 audio2 = r.record(source2)
 x2= r.recognize_google(audio2,language="ar-EG")
 reshaped_text2 = arabic_reshaper.reshape(x2)    # correct its shape
 bidi_text2 = get_display(reshaped_text2)   
 print(bidi_text2)
#  if  x[0:5]  == x2[0:5]:
#      print("yees")
#  else:
#      print("NO")


# # Return the Hamming distance between string1 and string2.
# # string1 and string2 should be the same length.
# def hamming_distance(string1, string2): 
#     # Start with a distance of zero, and count up
#     distance = 0
#     # Loop over the indices of the string
#     if len(string1)>len(string2):
#       L = len(string1)
#     else:
#       L=len(string2)
#     for i in range(L):
#         # Add 1 to the distance if these two characters are not equal
#         if string1[i] != string2[i]:
#             distance += 1
#     # Return the final count of differences
#     return distance


# print(hamming_distance(bidi_text1,bidi_text2))












   


