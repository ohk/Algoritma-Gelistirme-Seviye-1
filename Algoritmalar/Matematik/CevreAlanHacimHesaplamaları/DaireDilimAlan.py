import math
yaricap = float (input("çemberin yarıçap uzunluğunu giriniz: "))
aci = float(input("Daire diliminin açısını giriniz: "))
alan= (aci/360)*math.pi*yaricap*yaricap
alan = round(alan,4)
print("Yarıcapı {} ve açısı {} derece olan dairenin alanı = {}".format(yaricap,aci,alan))
