import math
import random

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

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
n = len(Dizi)
index = round(JumpSearch(Dizi, aranan, n))
if index > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}".format(Dizi,aranan,index))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı".format(Dizi,aranan))
