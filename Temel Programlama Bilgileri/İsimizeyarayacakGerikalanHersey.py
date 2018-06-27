import random
print(random.random())

harfler = ["a","b","c","d","e"]
print(harfler)
i=0
while i<len(harfler) and i<19:
    print(harfler[i])
    harfler.append(i)
    i = i + 1
    print(harfler)
print(harfler)
y=0
for t in range(1,7):
    y=y+2
    if t<5 or y == 6:
        print(t)
        print(y)
        print("Ben 2sinden birine eşit oldum.")
        y=2
sayilar = [[0,1,2],[0,1,3],[0,1,4]]
print(sayilar)
for i in range(0,3,1):
    for t in range(0,3,1):
        print(sayilar[i][t])
