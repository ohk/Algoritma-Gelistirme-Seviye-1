import random
import math

def haversine(lon1, lat1, lon2, lat2):
    # Decimal değerleri radyan cinsine çeviriyor
    lon1, lat1, merkezlon, merkezlat = map(math.radians, [lon1, lat1, lon2, lat2])
    # Haversine Formülü
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 +math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    # Dünyanın yarıçapı = 6371
    km = 6371* c
    return km
acildurum = 0
merkezlon = 39.9333635
merkezlat = 32.8597419


for i in range(0,100,1):
    lon1 = random.uniform(25.0,45.0)
    lat1 = random.uniform(25.0,45.0)
    tehditmi = random.randint(0, 1)
    if tehditmi == 1:
        EH = "TEHDİT"
    else:
        EH = "TEHDİT DEĞİL"
    print("Durum",i+1)
    print("Tehdit durumu:",EH)

    if haversine(lon1,lat1,merkezlon,merkezlat)>6500 or tehditmi == 0:
        print("Tespit edilen cismin kordinatları {},{}\nAramızdaki uzaklık: {}\nCismin uzaklığı tehdit içermemektedir.".format(lon1,lat1,haversine(lon1,lat1,merkezlon,merkezlat)))
    else:
        acildurum = acildurum+1
        print("Tespit edilen cismin kordinatları {},{}\nAramızdaki uzaklık: {}\nCismin uzaklığı tehdit içermektedir. Acil duruma geçilsin.".format(lon1,lat1,haversine(lon1,lat1,merkezlon,merkezlat)))
    print("\n------------------------------------------------------------------------\n")

print("{} cisimden tehdit olabilecek {} cisim tespit edilmiştir.".format(100,acildurum))
