import random
DNAsample = ["A","T","C","G"]
DNAcollection = []
eslesmeoranları = []
for i in range(1,200,1):
    Satir = []
    for t in range(0,300,1):
        Satir.append(random.sample(DNAsample,1))
    DNAcollection.append(Satir)

for t in range(1,199,1):
    eslesme = 0
    for a in range(0,300,1):
        if DNAcollection[0][a] == DNAcollection[t][a]:
            eslesme=eslesme+1
    eslesmeoran = eslesme/3
    eslesmeoran = round(eslesmeoran,3)
    print(t,". kişi hasta ile {} uyuşma sağladı.".format(eslesmeoran))
    eslesmeoranları.append(eslesmeoran)

enbuyuk = eslesmeoranları[0]
kisisirano = 1
for i in range(1,199,1):
    if eslesmeoranları[i-1]>enbuyuk:
        enbuyuk = eslesmeoranları[i-1]
        kisisirano = i+1
print(kisisirano,enbuyuk)
