def Fibonacci(n):
    if n<0:
        print("Yanlış sayı girdiniz")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

sayi = int(input("Kaçıncı elemanı öğrenmek istiyorsunuz: "))
print("{}. Fibonacci elemanı = {}".format(sayi,Fibonacci(sayi)))
