#SORU
#Bir radyo programında sorulan soruya cevap veren N kişiden, doğru cevabı veren ilk M kişiye ödül verilecektir.
    #a.Doğru cevabı, verilecek ödül sayısını, cevap veren kişi sayısını ve verilen cevapları okuyunuz.
    #b.Kazanan kişi sayısını hesaplayınız. Kazananların sıra numaralarını bir diziye yerleştiriniz.
    #c.Kazananların sıra numaralarını yazdırınız.

#ÇÖZÜM
cevaplist = []
odullist = []
verilecekodulsayi = int(input("Lütfen verilecek ödül sayısını giriniz: "))
dogrucevap= input("Doğru cevabı giriniz: ")
cevapverenkisisayisi = int(input("Cevap veren kişi sayısı: "))
for i in range(1,cevapverenkisisayisi+1,1):
    if dogrucevap == input("{}. cevap veren kişinin cevabını giriniz: ".format(i)):
        odullist.append(i)
if odullist.count> verilecekodulsayi:
    for i in range(1,verilecekodulsayi,1):
        print(odullist[i])
print("numaralı kişiler ödül almaya hak kazanmıştır.")
