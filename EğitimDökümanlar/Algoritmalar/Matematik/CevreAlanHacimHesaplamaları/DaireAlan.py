import math
yaricap = float (input("Dairenin yarıçap uzunluğunu giriniz: "))
alan= math.pi*yaricap*yaricap
alan = round(alan,4)
print("Yarıcapı {} olan dairenin alanı = {}".format(yaricap,alan))
