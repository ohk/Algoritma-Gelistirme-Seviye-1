import random

AnaDizi = []
SiralanmisDizi = []
dizielemansayisi = int (random.uniform(1,10))
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi
print("Dizi Eleman Sayısı:",dizielemansayisi)
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
            Adim = Adim +1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")


SelectionSort(SiralanmisDizi)
