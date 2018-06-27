import math
choosed2 = True

def FonkUcgenCevre():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    kenar3 = float (input("Üçüncü kenarın uzunluğunu giriniz: "))
    cevre=kenar1+kenar2+kenar3
    return print("Kenar uzunlukları {} ,{} ,{} olan üçgenin çevresi = {}".format(kenar1,kenar2,kenar3,cevre))

def FonkUcgen2KenarveAci3kenar():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    aci = float (input("İki kenar arasındaki açıyı giriniz: "))
    kenar3 = math.sqrt(kenar1*kenar1+kenar2*kenar2-2*kenar1*kenar2*math.cos(math.radians(aci)))
    return print("1. kenarı {},2. kenarı {} ve aralarındaki açı {} derece olan üçgenin 3. kenarı = {}".format(kenar1,kenar2,aci,kenar3))

def FonkUcgenAlan2KenarveDerece():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    aci = float (input("İki kenar arasındaki açıyı giriniz: "))
    alan = kenar1*kenar2*math.sin(math.radians(aci))*1/2
    return print("1. kenar uzunluğu {} , 2. kenar uzunluğu {} ve bu kenarlar arasındaki açı {} derece olan üçgenin alanı = {}".format(kenar1,kenar2,aci,alan))

def FonkUcgenAlan2kenarvedikAci():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    alan = (kenar1*kenar2)/2
    return print("1. kenar uzunluğu {} , 2. kenar uzunluğu {} ve bu kenarlar arasındaki açı {} derece olan üçgenin alanı = {}".format(kenar1,kenar2,90,alan))

def FonkUcgenAlanTumKenarlariBilinen():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    kenar3 = float (input("Üçüncü kenarın uzunluğunu giriniz: "))
    u=(kenar1+kenar2+kenar3)/2
    alan=math.sqrt(u*(u-kenar1)*(u-kenar2)*(u-kenar3))
    return print("Kenar uzunlukları {},{},{} olan üçgenin alanı = {}".format(kenar1,kenar2,kenar3,alan))

def checkchoosed():
    EH= input("Yeni bir hesaplama yapmak ister misiniz(Evet için E'ye, Hayır için H'ye basınız): ")
    if EH == "E":
        main(True)
    elif EH == "H":
        main(False)
    else:
        print("\nSeçiminiz belirlenen aralıkta değil! Lütfen yeniden seçim yapınız")
        checkchoosed()
    return


def main(choosed2):
    if choosed2 == True:
        print("\nÜçgenlerle ilgili yapmak istediğinizi seçiniz:")
        choosed = int(input("1. Üçgenin çevresini bulmak\n2. 2 kenarı ve açısı bilenen üçgenin 3. kenarını Bulmak\n3. 2 kenarı ve aralarındaki açı bilinen üçgenin alanını bulmak\n4. Dik üçgenin alanını bulmak\n5. Tüm kenarları bilinen üçgenin alanını bulmak\nSeçiminiz: "))

        if choosed == 1:
            FonkUcgenCevre()
        elif choosed == 2:
            FonkUcgen2KenarveAci3kenar()
        elif choosed == 3:
            FonkUcgenAlan2KenarveDerece()
        elif choosed == 4:
            FonkUcgenAlan2kenarvedikAci()
        elif choosed == 5:
            FonkUcgenAlanTumKenarlariBilinen()
        else:
            print("\nSeçiminiz belirlenen aralıkta değil! Lütfen yeniden seçim yapınız")
            main(True)
        checkchoosed()
    else:
        print("\nProgramımızı kullandığınız için teşekkür ederiz. İyi Günler - Ömer Hamid Kamışlı")
    return

main(choosed2)
