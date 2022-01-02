import arabic_reshaper
from bidi.algorithm import get_display
import speech_to_text
import csv
import re
import pandas as pd
import pyquran as q


class search_by_text(speech_to_text.To_Text):
    def __init__(self,data,samplingFrequency,duration):
        super().__init__(data,samplingFrequency,duration)
    def search_text(self,text):
          aya = q.quran.get_verse(sura_number=1, verse_number=2)
          for i in range (115):
            sora = q.quran.get_sura(i, with_tashkeel=False)
            for n in range(len(sora)):
                ayas = sora[n].split()
                if text in ayas:
                   print(i,sora)      





        
        # filename="qurantexttanzil.csv"
        # with open(filename, 'r',encoding="utf-8") as csvfile:
        #     csvreader = csv.reader(csvfile)
        #     print("search text process")
        #     search = open("qurantexttanzil.csv","r",encoding="utf8")
        #     df = pd.read_csv('qurantexttanzil.csv')
        #     Table= df.to_html("table.html")
        #     for line in search:
        #      if text in line:
        #             print("if")
        #             reshaped_text1 = arabic_reshaper.reshape(line)    # correct its shape
        #             bidi_text1 = get_display(reshaped_text1)           # correct its direction
        #             print(bidi_text1)
        #             length = len(bidi_text1)
        #             last = length-1
        #             print(bidi_text1[last-1]+bidi_text1[last-5])
            










                    
            # df = pd.read_csv('qurantexttanzil.csv')
            # df = df.select_dtypes(exclude='number')
            # print("line")
            # for line in df:
            #     if text in line:
            #           print("if")
            #           reshaped_text1 = arabic_reshaper.reshape(line)    # correct its shape
            #           bidi_text1 = get_display(reshaped_text1)           # correct its direction
            #           print(bidi_text1)   


