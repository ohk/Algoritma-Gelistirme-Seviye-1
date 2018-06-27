import random
from termcolor import colored,cprint
def randomGetir(Son):
    sayi = int(round(random.uniform(100,Son)))
    if sayi<10:
        return("  {}".format(sayi))
    elif sayi>10 and sayi<100:
        return(" {}".format(sayi))
    else:
        return("{}".format(sayi))
Country = ["CHINA","U.S.A","TURKEY","TAIWAN","BRAZIL","ROMANIA","INDIA","ITALY","HUNGARY","AUSTRALIA","AFGHANISTAN","BELGIUM"]
for i in range(100000000):
    print("Case:",i)
    print("-----------------------------------------------------------------------------")
    for t in range(1000000):
        tehditsayi = round(random.uniform(1,25))
    if tehditsayi>10:
        cprint("{}.{}.{}.{} ip adress detected.".format(randomGetir(255),randomGetir(255),randomGetir(255),randomGetir(255)),'cyan')
        cprint("Firewall : active\nSecurity Level : {} ".format(tehditsayi),'red')
    else:
        cprint("{}.{}.{}.{} ip adress detected.".format(randomGetir(255),randomGetir(255),randomGetir(255),randomGetir(255)),'cyan')
        cprint("Firewall : deactive\nSecurity Level : {} ".format(tehditsayi),'green')
    if tehditsayi%12 <7:
        cprint("Country: {}".format(Country[tehditsayi%12]),'yellow')
    else:
        cprint("Country: {}".format(Country[tehditsayi%12]),'blue')
    print("-----------------------------------------------------------------------------")
