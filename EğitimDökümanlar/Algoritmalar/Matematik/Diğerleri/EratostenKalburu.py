def AdimAdimEratostenKalburu(n):
    asal = [True for i in range(n+1)]
    asal2 = []
    adimSayisi = 1
    p = 2
    while (p * p <= n):
        print("Adım {} - {} için ".format(adimSayisi,p))
        print("----------------------------------------------")
        if (asal[p] == True):
            for i in range(p * 2, n+1, p):
                asal[i] = False
        p += 1
        for i in range(1,n,1):
            if i<10:
                if asal[i]==False:
                    print("|0{}".format(i)," - ",asal[i],"                                 |")
                else:
                    print("|0{}".format(i)," - ",asal[i],"                                  |")
            else:
                if asal[i]==False:
                    print("|{}".format(i)," - ",asal[i],"                                 |")
                else:
                    print("|{}".format(i)," - ",asal[i],"                                  |")

        print("----------------------------------------------")
        adimSayisi = adimSayisi+1
        
def EratostenKalburu(n):
    asal = [True for i in range(n+1)]
    asal2 = []
    p = 2
    while (p * p <= n):
        if (asal[p] == True):
            for i in range(p * 2, n+1, p):
                asal[i] = False
        p += 1
    for p in range(2, n):
        if asal[p]:
            asal2.append(p)
    print(asal2)

n=int(input("Kaça kadar asal sayıların bulunmasını istiyorsunuz: "))
AdimAdimEratostenKalburu(n)
print ("N'den küçük veya eşit asal sayılar: ",n)
EratostenKalburu(n)
