#Değişiklikler doğru ile yanlışların yeri değiştirildi. Analizin doğruluğu artsın diye
import random
Siklar = ["A", "B", "C", "D", "E"]
Cevaplar = []
dogrucevaplar = []
hangisorucokhata=[]
ogrencisayisi = int (input("Sınava giren öğrenci sayısı: "))
sorusayisi = int (input("Kaç soru soruldu: "))
for i in range(0,ogrencisayisi+1,1):
    Satir = []
    for t in range(0,sorusayisi,1):
        Satir.append(random.sample(Siklar,1))
    Cevaplar.append(Satir)
print(Cevaplar)
for i in range(0,ogrencisayisi,1):
    Satir = []
    truesayi = 0
    falsesayi = 0
    for t in range(0,sorusayisi,1):
        if Cevaplar[i][t] == Cevaplar[ogrencisayisi][t]:
            Satir.append(False)
            falsesayi = falsesayi +1
        else:
            Satir.append(True)
            truesayi= truesayi +1
    Satir.append(truesayi)
    Satir.append(falsesayi)
    dogrucevaplar.append(Satir)
print(dogrucevaplar)
for i in range(0,ogrencisayisi,1):
    net = (dogrucevaplar[i][sorusayisi]-dogrucevaplar[i][sorusayisi+1]-(dogrucevaplar[i][sorusayisi+1]/4))
    print("{}. öğrenci {} adet doğru {} adet yanlış yapmıştır. NET = {}".format(i+1,dogrucevaplar[i][sorusayisi],dogrucevaplar[i][sorusayisi+1],net))
#En çok hata yapılan soruyu bulma
for i in range(0,sorusayisi,1):
    hata = 0
    for t in range(0,ogrencisayisi,1):
        if dogrucevaplar[i][t] == False:
            hata = hata + 1
    hangisorucokhata.append(hata)
enbuyuk = hangisorucokhata[0]
hatasoruno = 1
for i in range(1,sorusayisi,1):
    if hangisorucokhata[i]>enbuyuk:
        enbuyuk = hangisorucokhata[i]
        hatasoruno = i+1
print("Bu denemedeki en çok yanlış yapılan soru {}. soru, yanlış yapılma sayısı {}".format(hatasoruno,enbuyuk))
