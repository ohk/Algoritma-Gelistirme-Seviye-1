sayi = int(input("Pozitif tam sayı: "))
print("{} sayısının tam bölenleri:".format(sayi))
print("1",end="")
for i in range(2,sayi+1):
    if(sayi%i == 0):
        print(",{}".format(i),end ="")
