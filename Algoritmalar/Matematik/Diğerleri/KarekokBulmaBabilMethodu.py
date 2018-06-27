sayi= int(input("Karekökü alınacak sayı: "))
e = float(input("Doğruluk seviyesi(Ne kadar küçükse o kadar iyi): "))
x = sayi
y = 1
while(x - y > e):
    x = (x + y)/2
    y = sayi/x
print("{} sayısının karekökü = {},doğruluk seviyesi= {}".format(sayi,x,e))
