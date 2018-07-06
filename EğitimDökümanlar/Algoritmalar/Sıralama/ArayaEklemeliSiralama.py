import random
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi
print(AnaDizi)
def InsertionSort(SiralanmisDizi):
    Adim = 1
    for i in range(1, len(SiralanmisDizi)):
        key = SiralanmisDizi[i]
        j = i-1
        girisadim = Adim
        while j >=0 and key < SiralanmisDizi[j] :
            print("Adım:",Adim,"(giriş) | ",SiralanmisDizi[j]," vs ",key," | i = ",i," | j = ",j," | ",SiralanmisDizi)
            SiralanmisDizi[j+1] = SiralanmisDizi[j]
            j -= 1
            SiralanmisDizi[j+1] = key
            print("Adım:",Adim,"(çıkış) | i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim +1
        if girisadim == Adim:
            print("Adım:",Adim,"(çıkış) | i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim+1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")

InsertionSort(SiralanmisDizi)
