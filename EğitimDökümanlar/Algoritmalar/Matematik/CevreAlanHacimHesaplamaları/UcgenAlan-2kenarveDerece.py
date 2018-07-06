import math
kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
aci = float (input("İki kenar arasındaki açıyı giriniz: "))
alan = kenar1*kenar2*math.sin(math.radians(aci))*1/2
print("1. kenar uzunluğu {} , 2. kenar uzunluğu {} ve bu kenarlar arasındaki açı {} derece olan üçgenin alanı = {}".format(kenar1,kenar2,aci,alan))
