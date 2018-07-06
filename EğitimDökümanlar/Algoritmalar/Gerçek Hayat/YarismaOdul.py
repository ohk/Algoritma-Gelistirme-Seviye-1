cevaplist = []
odullist = []
verilecekodulsayi = int(input("Lütfen verilecek ödül sayısını giriniz: "))
dogrucevap= input("Doğru cevabı giriniz: ")
cevapverenkisisayisi = int(input("Cevap veren kişi sayısı: "))
for i in range(1,cevapverenkisisayisi+1,1):
    if dogrucevap == input("{}. cevap veren kişinin cevabını giriniz: ".format(i)):
        odullist.append(i)
i = 0
if int(len(odullist))<(verilecekodulsayi-1):
    while i<= int(len(odullist))-1:
        print(odullist[i])
        i = i +1
else:
    while i<= verilecekodulsayi-1:
        print(odullist[i])
        i = i +1
print("numaralı kişiler ödül almaya hak kazanmıştır.")
