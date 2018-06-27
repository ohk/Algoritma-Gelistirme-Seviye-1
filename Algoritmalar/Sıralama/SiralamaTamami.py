import random
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi

def SelectionSort(SiralanmisDizi):
    Adim = 1
    for i in range(len(SiralanmisDizi)-1):
        for j in range(i+1,len(SiralanmisDizi)):
            print("Adım:",Adim,"(giriş) | i = ",i," | j = ",j," | ",SiralanmisDizi)
            if SiralanmisDizi[j]<SiralanmisDizi[i]:
                tmp = SiralanmisDizi[i]
                SiralanmisDizi[i] = SiralanmisDizi[j]
                SiralanmisDizi[j] = tmp
            print("Adım:",Adim,"(çıkış) | i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim+1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")

def BubbleSort(SiralanmisDizi):
    Adim = 1
    for i in range(len(SiralanmisDizi)):
        for j in range(len(SiralanmisDizi)-1):
            degisim = "yapılmadı"
            print("Adım:",Adim,"(giriş) | ",SiralanmisDizi[j+1]," vs ",SiralanmisDizi[j]," | i = ",i," | j = ",j," | ",SiralanmisDizi)
            if SiralanmisDizi[j+1] <SiralanmisDizi[j]:
                 tmp = SiralanmisDizi[j]
                 SiralanmisDizi[j] = SiralanmisDizi[j+1]
                 SiralanmisDizi[j+1] = tmp
                 degisim = "yapıldı"
            print("Adım:",Adim,"(çıkış) | degişim =",degisim,"| i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim+1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")

BubbleSort(SiralanmisDizi)
