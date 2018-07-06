sayi1 = int(input("Üssü alınacak sayıyı giriniz: "))
sayi2 = int(input("Üssü giriniz: "))

if(sayi2==0):
    cevap = 1

cevap=sayi1
artis=sayi1

for i in range(1,sayi2):
    print("Adim:",i)
    print(artis,"+ (",end="")
    for j in range (1,sayi1):
        if j == (sayi1-1):
            cevap+=artis
            print(artis,")")
        else:
            cevap+=artis
            print(artis,"+",end="")
    artis=cevap
    print("Bir sonraki adımda adımda artış miktarı",artis)
    
print("{} üzeri {} = {}".format(sayi1,sayi2,cevap))
