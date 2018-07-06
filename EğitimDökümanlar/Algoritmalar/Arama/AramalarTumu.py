import math
import random

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
n = len(Dizi)

def LinearSearch(Dizi, aranan):
    for i in range(len(Dizi)):
        if Dizi[i] == aranan:
            return i
    return -1

def JumpSearch( Dizi , aranan , n ):
    adim = math.sqrt(n)
    onceki = 0
    while Dizi[int(min(adim, n)-1)] < aranan:
        onceki = adim
        adim += math.sqrt(n)
        if onceki >= n:
            return -1
    while Dizi[int(onceki)] < aranan:
        onceki += 1
        if onceki == min(adim, n):
            return -1
    if Dizi[int(onceki)] == aranan:
        return onceki
    return -1

def BinarySearch (Dizi, sol, sag, aranan):
    if sag >= sol:
        ortanca = sol + (sag - sol)//2
        ortanca = int(ortanca)
        if Dizi[ortanca] == aranan:
            return ortanca
        elif Dizi[ortanca] > aranan:
            return BinarySearch(Dizi, sol, ortanca-1, aranan)
        else:
            return BinarySearch(Dizi, ortanca+1, sag, aranan)

    else:
        return -1

def interpolationSearch(Dizi, n, aranan):
    dusuk = 0
    yuksek = (n - 1)
    while dusuk <= yuksek and aranan >= Dizi[dusuk] and aranan <= Dizi[yuksek]:
        pos  = dusuk + int(((float(yuksek - dusuk)/( Dizi[yuksek] - Dizi[dusuk])) * ( aranan - Dizi[dusuk])))
        if Dizi[pos] == aranan:
            return pos
        if Dizi[pos] < aranan:
            dusuk = pos + 1;
        else:
            yuksek = pos - 1;
    return -1

def ExponentialSearch(Dizi, n, aranan):
    if Dizi[0] == aranan:
        return 0
    i = 1
    while i < n and Dizi[i] <= aranan:
        i = i * 2
    return BinarySearch( Dizi, i / 2, min(i, n), aranan)

def Chooser():
    print("Hangi arama yöntemini kullanacaksınız?")
    print("1. Linear Search ( Doğrusal Arama )\n2. Jump Search ( Atlamalı Arama )\n3. Binary Search ( ikili Arama )\n4. Interpolation Search ( Enterpolasyon Arama )\n5. Exponantional Search ( Üssel Arama )")
    cevap = int(input())
    if cevap == 1:
        index = LinearSearch(Dizi,aranan)
    elif cevap == 2:
        index = JumpSearch(Dizi,aranan,n)
    elif cevap == 3:
        index = BinarySearch(Dizi,0,len(Dizi)-1,aranan)
    elif cevap == 4:
        index = interpolationSearch(Dizi,n,aranan)
    elif cevap == 5:
        index = ExponentialSearch(Dizi,n,aranan)
    else:
        print("Seçiminizi yeniden yapınız. Yaptığınız seçimi gerçekleştiremiyorum\n")
        Chooser()
    return index

indexdonen = int(Chooser())
if indexdonen > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}\n".format(Dizi,aranan,indexdonen))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı\n".format(Dizi,aranan))
