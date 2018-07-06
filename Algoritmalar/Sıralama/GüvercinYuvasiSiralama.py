import random
AnaDizi = []
SiralanmisDizi = []
#dizielemansayisi = int (random.uniform(1,50))
dizielemansayisi = 5
for i in range(0,dizielemansayisi,1):
    AnaDizi.append(int(random.uniform(1,250)))
SiralanmisDizi = AnaDizi

print("\n Ana Dizi = ",end = "")
for i in range(len(AnaDizi)):
    if i+1 ==len(AnaDizi):
        print(AnaDizi[i],end = "")
    else:
        print(AnaDizi[i],end = ",")

def PigeonholeSort(SiralanmisDizi):
    my_min = min(SiralanmisDizi)
    my_max = max(SiralanmisDizi)
    size = my_max - my_min + 1
    holes = [0] * size
    for t in SiralanmisDizi:
        holes[t - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            SiralanmisDizi[i] = count + my_min
            i += 1

PigeonholeSort(SiralanmisDizi)
print("\n Sıralanmış dizi = ",end = "")
for i in range(len(SiralanmisDizi)):
    if i+1 ==len(SiralanmisDizi):
        print(SiralanmisDizi[i],end = "")
    else:
        print(SiralanmisDizi[i],end = ",")
