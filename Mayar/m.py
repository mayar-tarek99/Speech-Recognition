import pyquran as q
aya = q.quran.get_verse(sura_number=1, verse_number=2)
#sora = q.quran.get_sura(108, with_tashkeel=False)
#print(sora)
rev_sora = []
name = 'الكوثر'
for i in range (115):
    sora = q.quran.get_sura(i, with_tashkeel=False)
    for n in range(len(sora)):
        ayas = sora[n].split()
        if name in ayas:
            print(ayas,i,sora)