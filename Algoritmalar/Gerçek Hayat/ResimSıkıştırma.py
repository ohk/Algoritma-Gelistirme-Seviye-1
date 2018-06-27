import random
fotograf = []
zipped = []

for i in range(0,500,1):
    Satir = []
    for t in range(0,500,1):
        Satir.append(round(random.uniform(0,255),0))
    fotograf.append(Satir)

for i in range(0,500,1):
    for t in range(0,500,1):
        Satir = []
        if fotograf[i][t] != 0:
            Satir.append(i)
            Satir.append(t)
            Satir.append(fotograf[i][t])
            zipped.append(Satir)

print("orjinal",250000)
print("Sıkıştırılmış",len(zipped))
