#Bir dizi içerisinde elimizdeki kolilerin kiloları bulunmaktadır. Araçlarımız maksimum 300 kilo
#taşıyabiliyor. 300 kiloyu aşan her yük için yeni araç gerekmektedir.
#Verilen diziye göre kaç araca ihtiyaç vardır.
import random
yuksample = [5,10,15,20,25,30,35,40,7,14,21,28,35]
yuksayisi = random.randint(0,100)
yukler = []
for i in range(0,yuksayisi,1):
    yukler.append(random.sample(yuksample,1))
aracsayisi = 1
aracmevcutkilo = 0
i=0
print("Yük sayısı:",yuksayisi)
print("Yükler:\n",yukler)
while i<(yuksayisi-1):
    TMP = aracmevcutkilo + int(yukler[i][0])
    if TMP<=300:
        aracmevcutkilo = TMP
        i = i +1
    else:
        aracsayisi = aracsayisi + 1
        aracmevcutkilo = 0
if aracmevcutkilo>0:
    aracmevcutkilo = 0
    aracsayisi=aracsayisi+1
print("Toplam kullanılan araç sayısı= {}".format(aracsayisi))
