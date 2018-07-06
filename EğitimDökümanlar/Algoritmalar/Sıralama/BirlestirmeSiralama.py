import random
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi

print("\nAna Dizi = ",end = "")
for i in range(len(AnaDizi)):
    if i+1 ==len(AnaDizi):
        print(AnaDizi[i],end = "")
    else:
        print(AnaDizi[i],end = ",")
print("\n")

def MergeSort(SiralanmisDizi):
    print("----------------------")
    print(SiralanmisDizi)
    lendizi = len(SiralanmisDizi)
    if len(SiralanmisDizi)>1:
        orta = len(SiralanmisDizi)//2
        sag = SiralanmisDizi[orta:]
        sol = SiralanmisDizi[:orta]
        MergeSort(sag)
        MergeSort(sol)
        i=0
        j=0
        k=0
        while i<len(sol) and j<len(sag):
            if sol[i]<sag[j]:
                SiralanmisDizi[k]=sol[i]
                i = i +1
            else:
                SiralanmisDizi[k] = sag[j]
                j = j + 1
            k = k + 1
            print("While 1",SiralanmisDizi)
        while i<len(sol):
            SiralanmisDizi[k]=sol[i]
            i = i+1
            k = k+1
            print("While 2",SiralanmisDizi)
        while j<len(sag):
            SiralanmisDizi[k]=sag[j]
            j = j+1
            k = k+1
            print("While 3",SiralanmisDizi)
        print("While Sonrası",SiralanmisDizi)
    print("If Sonrası",SiralanmisDizi)
    if lendizi == len(AnaDizi):
        print("\n Sıralanmış dizi = ",end = "")
        for i in range(len(SiralanmisDizi)):
            if i+1 ==len(SiralanmisDizi):
                print(SiralanmisDizi[i],end = "")
            else:
                print(SiralanmisDizi[i],end = ",")
MergeSort(SiralanmisDizi)
