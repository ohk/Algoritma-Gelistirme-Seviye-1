import math
yaricap = float (input("Dairenin yarıçap uzunluğunu giriniz: "))
cevre = 2*math.pi*yaricap
cevre = round(cevre,4)
print("Yarıcapı {} olan dairenin çevresi = {}".format(yaricap,cevre))
