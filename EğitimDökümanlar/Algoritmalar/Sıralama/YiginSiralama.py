import random
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

print("\n")
def HeapSort(SiralanmisDizi):

    def heapify(SiralanmisDizi, n, i):
        ebuyuk = i
        l = 2 * i + 1
        r = 2 * i + 2
        print("------------------------------------------")
        print("i",i)
        if l < n and SiralanmisDizi[i] < SiralanmisDizi[l]:
            print("l",l,"n",n,"SiralanmisDizi[i]",SiralanmisDizi[i],"SiralanmisDizi[l]",SiralanmisDizi[l])
            ebuyuk = l
            print("1. if için:",SiralanmisDizi)
        if r < n and SiralanmisDizi[ebuyuk] < SiralanmisDizi[r]:
            print("r",r,"n",n,"SiralanmisDizi[i]",SiralanmisDizi[i],"SiralanmisDizi[r]",SiralanmisDizi[r])
            ebuyuk = r
            print("2. if için:",SiralanmisDizi)
        if ebuyuk != i:
            print("ebuyuk",ebuyuk,"i",i,"SiralanmisDizi[i]",SiralanmisDizi[i],"SiralanmisDizi[ebuyuk]",SiralanmisDizi[ebuyuk])
            SiralanmisDizi[i],SiralanmisDizi[ebuyuk] = SiralanmisDizi[ebuyuk],SiralanmisDizi[i]
            heapify(SiralanmisDizi, n, ebuyuk)
            print("3. if için:",SiralanmisDizi)
    n = len(SiralanmisDizi)
    for i in range(n, -1, -1):
        heapify(SiralanmisDizi, n, i)
    for i in range(n-1, 0, -1):
        SiralanmisDizi[i], SiralanmisDizi[0] = SiralanmisDizi[0], SiralanmisDizi[i]
        heapify(SiralanmisDizi, i, 0)

HeapSort(SiralanmisDizi)

print("\n Sıralanmış dizi = ",end = "")
for i in range(len(SiralanmisDizi)):
    if i+1 ==len(SiralanmisDizi):
        print(SiralanmisDizi[i],end = "")
    else:
        print(SiralanmisDizi[i],end = ",")
