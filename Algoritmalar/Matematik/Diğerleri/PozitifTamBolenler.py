sayi = int(input("Pozitif tam sayı: "))
print("{} sayısının tam bölenleri:".format(sayi))
for i in range(1,sayi+1):
    if(sayi%i == 0):
        print("{}".format(i))
