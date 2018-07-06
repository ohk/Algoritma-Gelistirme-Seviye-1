import random
AnaDizi = []
SiralanmisDizi = []
dizielemansayisi = int (random.uniform(1,50))
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi
print(AnaDizi)

def CombSort(SiralanmisDizi):
    def getNextGap(gap):
        gap = (gap * 10)/13
        if gap < 1:
            return 1
        return gap

    Adim = 1
    n = int(len(SiralanmisDizi))
    gap = n
    degistimi = True
    while gap !=1 or degistimi == True:
        gap = int(getNextGap(gap))
        degistimi = False
        degisim = "yapılmadı"
        for i in range(0, n-gap):
            print("Adım:",Adim,"(giriş) | gap = ",gap," | ",SiralanmisDizi[i + gap]," vs ",SiralanmisDizi[i]," | ",SiralanmisDizi)
            if SiralanmisDizi[i] > SiralanmisDizi[i + gap]:
                SiralanmisDizi[i], SiralanmisDizi[i + gap]=SiralanmisDizi[i + gap], SiralanmisDizi[i]
                degistimi = True
                degisim = "yapıldı"
            print("Adım:",Adim,"(çıkış) | degişim =",degisim)
            Adim = Adim +1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")


CombSort(SiralanmisDizi)
