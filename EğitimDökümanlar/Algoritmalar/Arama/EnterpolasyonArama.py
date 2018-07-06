import random
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
    

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
index = interpolationSearch(Dizi,len(Dizi),aranan)

if index > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}".format(Dizi,aranan,index))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı".format(Dizi,aranan))
