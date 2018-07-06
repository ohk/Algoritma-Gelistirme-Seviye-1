import random
Siklar = ["A", "B", "C", "D", "E"]
Cevaplar = []
dogrucevaplar = []
ogrencisayisi = int (input("Sınava giren öğrenci sayısı: "))
sorusayisi = int (input("Kaç soru soruldu: "))
for i in range(0,ogrencisayisi+1,1):
    Satir = []
    for t in range(0,sorusayisi,1):
        Satir.append(random.sample(Siklar,1))
    Cevaplar.append(Satir)
for i in range(0,ogrencisayisi,1):
    Satir = []
    truesayi = 0
    falsesayi = 0
    for t in range(0,sorusayisi,1):
        if Cevaplar[i][t] == Cevaplar[ogrencisayisi][t]:
            Satir.append(True)
            truesayi= truesayi +1
        else:
            Satir.append(False)
            falsesayi = falsesayi +1
    Satir.append(truesayi)
    Satir.append(falsesayi)
    dogrucevaplar.append(Satir)
for i in range(0,ogrencisayisi,1):
    net = (dogrucevaplar[i][sorusayisi]-dogrucevaplar[i][sorusayisi+1]-(dogrucevaplar[i][sorusayisi+1]/4))
    print("{}. öğrenci {} adet doğru {} adet yanlış yapmıştır. NET = {}".format(i+1,dogrucevaplar[i][sorusayisi],dogrucevaplar[i][sorusayisi+1],net))
