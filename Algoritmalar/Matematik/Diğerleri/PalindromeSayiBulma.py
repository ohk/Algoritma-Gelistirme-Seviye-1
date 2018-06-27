def basamak(sayi):
    sayac=1
    while sayi>=10:
        sayac+=1
        sayi=sayi/10
    return sayac

palindrome = []
sayidizi = []
sayi = int(input("Hangi sayıya kadar bulunacak?"))
basamaksayi=basamak(sayi)
for i in range(10,sayi,1):
    if basamaksayi%2 == 0:
        for t in range(1,basamaksayi+1,1):
            tmp = sayi%pow(10,t)
            sayidizi.append(tmp)
        a=0
        while sayidizi[a] == sayidizi[basamaksayi-1] & a<=basamaksayi:
            a=a+1
            basamaksayi = basamaksayi-1
        if a == basamaksayi:
            palindrome.append(i)
    else:
        for t in range(1,basamaksayi+1,1):
            tmp = sayi%pow(10,t)
            sayidizi.append(tmp)
        a=0
        while sayidizi[a] == sayidizi[basamaksayi-1] & a<basamaksayi:
            a=a+1
            basamaksayi = basamaksayi-1
        if a == basamaksayi:
            palindrome.append(i)
print(palindrome)
