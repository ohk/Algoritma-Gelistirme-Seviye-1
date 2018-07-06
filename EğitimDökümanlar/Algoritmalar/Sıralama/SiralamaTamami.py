import random
AnaDizi = []
SiralanmisDizi = []
dizielemansayisi = int (random.uniform(1,50))
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))

SiralanmisDizi = AnaDizi.copy()

def AnaDizi2():
    print("\n Ana Dizi = ",end = "")
    for i in range(len(AnaDizi)):
        if i+1 ==len(AnaDizi):
            print(AnaDizi[i],end = "\n")
        else:
            print(AnaDizi[i],end = ",")

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

def CombSort(SiralanmisDizi):
    def getNextGap(gap):
        # Küçültme yapılıyor. Küçülte faktörü kullanılarak
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

def InsertionSort(SiralanmisDizi):
    Adim = 1
    for i in range(1, len(SiralanmisDizi)):
        key = SiralanmisDizi[i]
        j = i-1
        girisadim = Adim
        while j >=0 and key < SiralanmisDizi[j] :
            degisim = "yapılmadı"
            print("Adım:",Adim,"(giriş) | ",key," vs ",SiralanmisDizi[j]," | i = ",i," | j = ",j," | ",SiralanmisDizi)
            SiralanmisDizi[j+1] = SiralanmisDizi[j]
            j -= 1
            SiralanmisDizi[j+1] = key
            print("Adım:",Adim,"(çıkış) | i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim +1
        if girisadim == Adim:
            print("Adım:",Adim,"Gereksinimleri karşılamadı. Girdiği gibi çıktı.")
            Adim = Adim+1

def ShellSort(SiralanmisDizi):
    Adim = 1
    n = int(len(SiralanmisDizi))
    gap = int(round((n+1)//2))
    while gap > 0:
        girisadim = Adim
        for i in range(gap,n):
            temp = SiralanmisDizi[i]
            j = i
            while  j >= gap and SiralanmisDizi[j-gap] >temp:
                print("Adım:",Adim,"(giriş) | ",temp," vs ",SiralanmisDizi[j-gap]," | i = ",i," | j = ",j," | ",SiralanmisDizi)
                SiralanmisDizi[j] = SiralanmisDizi[j-gap]
                j -= gap
                print("Adım:",Adim,"(çıkış) | i = ",i," | j = ",j," | ",SiralanmisDizi)
                Adim = Adim + 1
            SiralanmisDizi[j] = temp
            if Adim == girisadim:
                print("Adım:",Adim,"Gereksinimleri karşılamadı. Girdiği gibi çıktı.")
                Adim = Adim + 1
        gap //= 2

def MergeSort(SiralanmisDizi):
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
        while i<len(sol):
            SiralanmisDizi[k]=sol[i]
            i = i+1
            k = k+1
        while j<len(sag):
            SiralanmisDizi[k]=sag[j]
            j = j+1
            k = k+1

def QuickSort(SiralanmisDizi,sol,sag):

    def partition(SiralanmisDizi,sol,sag):
        i = ( sol-1 )
        pivot = SiralanmisDizi[sag]
        for j in range(sol , sag):
            if   SiralanmisDizi[j] <= pivot:
                i = i+1
                SiralanmisDizi[i],SiralanmisDizi[j] = SiralanmisDizi[j],SiralanmisDizi[i]
        SiralanmisDizi[i+1],SiralanmisDizi[sag] = SiralanmisDizi[sag],SiralanmisDizi[i+1]
        return ( i+1 )

    if sol < sag:
        pF = partition(SiralanmisDizi,sol,sag)
        QuickSort(SiralanmisDizi, sol, pF-1)
        QuickSort(SiralanmisDizi, pF+1, sag)

def HeapSort(SiralanmisDizi):

    def heapify(SiralanmisDizi, n, i):
        ebuyuk = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and SiralanmisDizi[i] < SiralanmisDizi[l]:
            ebuyuk = l
        if r < n and SiralanmisDizi[ebuyuk] < SiralanmisDizi[r]:
            ebuyuk = r
        if ebuyuk != i:
            SiralanmisDizi[i],SiralanmisDizi[ebuyuk] = SiralanmisDizi[ebuyuk],SiralanmisDizi[i]
            heapify(SiralanmisDizi, n, ebuyuk)

    n = len(SiralanmisDizi)
    for i in range(n, -1, -1):
        heapify(SiralanmisDizi, n, i)
    for i in range(n-1, 0, -1):
        SiralanmisDizi[i], SiralanmisDizi[0] = SiralanmisDizi[0], SiralanmisDizi[i]
        heapify(SiralanmisDizi, i, 0)

def PigeonholeSort(SiralanmisDizi):
    my_min = min(SiralanmisDizi)
    my_max = max(SiralanmisDizi)
    size = my_max - my_min + 1
    holes = [0] * size
    for t in SiralanmisDizi:
        assert type(t) is int, "integers only please"
        holes[t - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            SiralanmisDizi[i] = count + my_min
            i += 1

def Chooser():
    print("Dizinizi hangi sıralama türüyle sıralamak istersiniz.\n1. Selection Sort (Seçme Sıralama)\n2. Bubble Sort (Kabarcık Sıralama)\n3. Comb Sort (Tarak Sıralama)\n4. Insertion Sort (Araya Eklemeli Sıralama)\n5. Shell Sort (Kabuk Sıralama)\n6. Merge Sort (Birleştirme Sıralama)\n7. Quick Sort (Hızlı Sıralama)\n8. Heap Sort (Yığın Sıralama)\n9. Pigeonhole Sort (Güvercin Yuvası Sıralama)")
    cevap = int(input())
    if cevap == 1:
        AnaDizi2()
        SelectionSort(SiralanmisDizi)
    elif cevap == 2:
        AnaDizi2()
        BubbleSort(SiralanmisDizi)
    elif cevap == 3:
        AnaDizi2()
        CombSort(SiralanmisDizi)
    elif cevap == 4:
        AnaDizi2()
        InsertionSort(SiralanmisDizi)
    elif cevap == 5:
        AnaDizi2()
        ShellSort(SiralanmisDizi)
    elif cevap == 6:
        AnaDizi2()
        MergeSort(SiralanmisDizi)
    elif cevap == 7:
        AnaDizi2()
        QuickSort(SiralanmisDizi)
    elif cevap == 8:
        AnaDizi2()
        HeapSort(SiralanmisDizi)
    elif cevap == 9:
        AnaDizi2()
        PigeonholeSort(SiralanmisDizi)
    else:
        print("Seçiminizi yeniden yapınız. Yaptığınız seçimi gerçekleştiremiyorum\n")
        Chooser()


Chooser()

print("\n Sıralanmış dizi = ",end = "")
for i in range(len(SiralanmisDizi)):
    if i+1 ==len(SiralanmisDizi):
        print(SiralanmisDizi[i],end = "")
    else:
        print(SiralanmisDizi[i],end = ",")
