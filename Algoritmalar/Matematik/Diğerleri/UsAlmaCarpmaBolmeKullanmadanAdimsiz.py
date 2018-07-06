sayi1 = int(input("Üssü alınacak sayıyı giriniz: "))
sayi2 = int(input("Üssü giriniz: "))

if(sayi2==0):
    cevap = 1

cevap=sayi1
artis=sayi1

for i in range(1,sayi2):
    for j in range (1,sayi1):
            cevap+=artis
    artis=cevap

print("{} üzeri {} = {}".format(sayi1,sayi2,cevap))
