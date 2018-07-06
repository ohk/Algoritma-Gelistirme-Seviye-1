def basamak(sayi):
    sayac=1
    while sayi>=10:
        sayac+=1
        sayi=sayi/10
    return sayac

palindrome = []
sayidizi = []
sayi = int(input("Hangi sayıya kadar bulunacak?"))
for i in range(10,sayi,1):
    basamaksayi=basamak(i)
    print("Sayı:",sayi,"Basamak",basamaksayi)
    if basamaksayi%2 == 0:
        for t in range(1,basamaksayi+1,1):
            tmp = i%pow(10,t)
            print("tmp",tmp)
            sayidizi.append(tmp)
        a=0
        while sayidizi[a] == sayidizi[basamaksayi-1] & a<=basamaksayi:
            print("a",sayidizi[a],"basamak a",sayidizi[basamaksayi-1])
            a=a+1
            basamaksayi = basamaksayi-1
        print("basamak",basamaksayi,"a",a)
        if a == basamaksayi/2:
            palindrome.append(i)
    else:
        for t in range(1,basamaksayi+1,1):
            tmp = i%pow(10,t)
            print("tmp",tmp)
            sayidizi.append(tmp)
        a=0
        while sayidizi[a] == sayidizi[basamaksayi-1] & a<basamaksayi:
            print("a",sayidizi[a],"basamak a",sayidizi[basamaksayi-1])
            a=a+1
            basamaksayi = basamaksayi-1
        print("basamak",basamaksayi,"a",a)
        if a == (round(basamaksayi/2)-1):
            print(a,basamaksayi)
            palindrome.append(i)
    print("------------------------------")
print(palindrome)
