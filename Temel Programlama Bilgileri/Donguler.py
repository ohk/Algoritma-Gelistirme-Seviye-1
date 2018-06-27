x = 5
y = 9

if x<7:
    print("if e girdi")
    print(x+y)
elif y<11:
    print("elif")
    print(y)
else:
    print("else e girdi")
    print(y-x)

for i in range(1,11,1):
    print("{}. adımdayım {} {}".format(i,x,y))
    print("{0}. adımdayım {2} {1}".format(i,x,y))

dogrumu = True
i = 0
while dogrumu == True:
    print("\n --------------------------------------------")
    print("While döngüsüne girdim. i =",i)
    print(dogrumu)
    if i == 15:
        dogrumu = False
    i = i + 1
    print(dogrumu)
    print("While döngüsünden çıkıyorum. Yeni i = {}".format(i))
    print("\n --------------------------------------------")
