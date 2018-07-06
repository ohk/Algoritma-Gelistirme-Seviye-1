import random

AnaDizi = []
SiralanmisDizi = []
dizielemansayisi = int (random.uniform(1,10))
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi
print("Dizi Eleman Sayısı:",dizielemansayisi)

def BubbleSort(SiralanmisDizi):
    Adim = 1
    for i in range(len(SiralanmisDizi)):
        for j in range(len(SiralanmisDizi)-i-1):
            degisim = "yapılmadı"
            print("Adım:",Adim,"(giriş) | ",SiralanmisDizi[j]," vs ",SiralanmisDizi[j+1]," | i = ",i," | j = ",j," | ",SiralanmisDizi)
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
