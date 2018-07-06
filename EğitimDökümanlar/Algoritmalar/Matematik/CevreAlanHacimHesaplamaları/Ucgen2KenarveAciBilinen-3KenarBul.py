import math
kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
aci = float (input("İki kenar arasındaki açıyı giriniz: "))
kenar3 = math.sqrt(kenar1*kenar1+kenar2*kenar2-2*kenar1*kenar2*math.cos(math.radians(aci)))
print("1. kenarı {},2. kenarı {} ve aralarındaki açı {} derece olan üçgenin 3. kenarı = {}".format(kenar1,kenar2,aci,kenar3))
