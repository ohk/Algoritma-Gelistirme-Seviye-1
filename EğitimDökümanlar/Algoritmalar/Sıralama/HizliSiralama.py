import random
import math
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi

print("\n Ana Dizi = ",end = "")
for i in range(len(AnaDizi)):
    if i+1 ==len(AnaDizi):
        print(AnaDizi[i],end = "")
    else:
        print(AnaDizi[i],end = ",")

def quickSort(SiralanmisDizi,sol,sag):

    def partition(SiralanmisDizi,sol,sag):
        print("\n----------------------------")
        i = ( sol-1 )
        pivot = SiralanmisDizi[sag]
        for j in range(sol , sag):
            print("pivot",pivot,"vs","SiralanmisDizi[j]",SiralanmisDizi[j])
            if   SiralanmisDizi[j] <= pivot:
                print("IF içine girdi")
                print("i:",i,"j:",j)
                i = i+1
                print("Sıralanmış Dizi[i]:",SiralanmisDizi[i],"SiralanmisDizi[j]:",SiralanmisDizi[j])
                SiralanmisDizi[i],SiralanmisDizi[j] = SiralanmisDizi[j],SiralanmisDizi[i]
                print("Değişim Yapıldıktan Sonra")
                print("Sıralanmış Dizi[i]:",SiralanmisDizi[i],"SiralanmisDizi[j]:",SiralanmisDizi[j])
        print("Fordan çıkıldı.")
        print("SiralanmisDizi[i+1]:",SiralanmisDizi[i+1],"SiralanmisDizi[sag]:",SiralanmisDizi[sag])
        SiralanmisDizi[i+1],SiralanmisDizi[sag] = SiralanmisDizi[sag],SiralanmisDizi[i+1]
        print("Değişim Yapıldıktan Sonra")
        print("SiralanmisDizi[i+1]:",SiralanmisDizi[i+1],"SiralanmisDizi[sag]:",SiralanmisDizi[sag])
        print(SiralanmisDizi)
        return ( i+1 )

    if sol < sag:
        pF = partition(SiralanmisDizi,sol,sag)
        quickSort(SiralanmisDizi, sol, pF-1)
        quickSort(SiralanmisDizi, pF+1, sag)

quickSort(SiralanmisDizi,0,len(SiralanmisDizi)-1)

print("\n Sıralanmış dizi = ",end = "")
for i in range(len(SiralanmisDizi)):
    if i+1 ==len(SiralanmisDizi):
        print(SiralanmisDizi[i],end = "")
    else:
        print(SiralanmisDizi[i],end = ",")
