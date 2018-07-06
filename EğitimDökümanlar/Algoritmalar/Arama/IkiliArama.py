import random
def BinarySearch (Dizi, sol, sag, aranan):
    if sag >= sol:
        ortanca = sol + (sag - sol)//2
        ortanca = int(ortanca)
        if Dizi[ortanca] == aranan:
            print(Dizi[sol:(ortanca-1)],"\nsol",sol,"\nsağ",ortanca-1,"\naranan",aranan)
            return ortanca
        elif Dizi[ortanca] > aranan:
            print(Dizi[sol:(ortanca-1)],"\nsol",sol,"\nsağ",ortanca-1,"\naranan",aranan)
            print("---------------------------------------------------------------")
            return BinarySearch(Dizi, sol, ortanca-1, aranan)
        else:
            print(Dizi[(ortanca+1):sag],"\nsol",ortanca+1,"\nsağ",sag,"\naranan",aranan)
            print("---------------------------------------------------------------")
            return BinarySearch(Dizi, ortanca+1, sag, aranan)
    else:
        return -1

Dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(Dizi,1)
aranan = int(randomsample[0])
n = len(Dizi)
print(Dizi,"\nsol",0,"\nsağ",len(Dizi)-1,"\naranan",aranan)
print("---------------------------------------------------------------")
print("\n")
index = BinarySearch(Dizi,0,len(Dizi)-1,aranan)
if index > -1:
    print("Dizi: {}\nAranan İfade = {}\nİfadenin İndexi = {}".format(Dizi,aranan,index))
else:
    print("Dizi: {}\nAranan İfade = {}\nİfade bulunamadı".format(Dizi,aranan))
