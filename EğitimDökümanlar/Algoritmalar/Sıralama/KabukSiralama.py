import random
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi

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
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")
ShellSort(SiralanmisDizi)
