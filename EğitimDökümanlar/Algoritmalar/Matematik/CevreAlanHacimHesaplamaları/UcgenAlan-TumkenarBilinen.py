import math
kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
kenar3 = float (input("Üçüncü kenarın uzunluğunu giriniz: "))
u=(kenar1+kenar2+kenar3)/2
print(u)
alan=math.sqrt(u*(u-kenar1)*(u-kenar2)*(u-kenar3))
print("Kenar uzunlukları {},{},{} olan üçgenin alanı = {}".format(kenar1,kenar2,kenar3,alan))
