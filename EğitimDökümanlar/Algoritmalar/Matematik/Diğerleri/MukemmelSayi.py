#Kendisi hariç bütün pozitif tam sayı çarpanları toplamı kendisine eşit olan sayılara denir.
sayi = int(input("Hangi sayının mükemmel olup olmadığını bulmak istersiniz: "))
t=0
for i in range(1,sayi):
    if sayi%i == 0:
        print(i)
        t=t+i
if sayi == t:
    print("{} mükemmel sayıdır.".format(sayi))
else:
    print("{} mükemmel sayı değildir.".format(sayi))
