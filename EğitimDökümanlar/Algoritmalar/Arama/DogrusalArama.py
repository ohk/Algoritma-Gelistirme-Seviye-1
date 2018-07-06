import random

def LinearSearch(Dizi, aranan):
    for i in range(len(Dizi)):
        if Dizi[i] == aranan:
            return i
    return -1

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
index = LinearSearch(Dizi, aranan)

if index > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}".format(Dizi,aranan,index))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı".format(Dizi,aranan))
