#Bubble Sort
#Kabarcık sıralamasında baştan sonra veya sondan başa doğru komşu
#elemanlar karşılaştırılarak büyüklük küçüklük durumlarına göre
#yerleri değiştirilir.

def BubbleSort(SiralanmisDizi):
    Adim = 1
    for i in range(len(SiralanmisDizi)):
        for j in range(len(SiralanmisDizi)-1):
            degisim = "yapılmadı"
            print("Adım:",Adim,"(giriş) | ",SiralanmisDizi[j+1]," vs ",SiralanmisDizi[j]," | i = ",i," | j = ",j," | ",SiralanmisDizi)
            if SiralanmisDizi[j+1] <SiralanmisDizi[j]:
                 tmp = SiralanmisDizi[j]
                 SiralanmisDizi[j] = SiralanmisDizi[j+1]
                 SiralanmisDizi[j+1] = tmp
                 degisim = "yapıldı"
            print("Adım:",Adim,"(çıkış) | degişim =",degisim,"| i = ",i," | j = ",j," | ",SiralanmisDizi)
            Adim = Adim+1
    print("\n Sıralanmış dizi = ",end = "")
    for i in range(len(SiralanmisDizi)):
        if i+1 ==len(SiralanmisDizi):
            print(SiralanmisDizi[i],end = "")
        else:
            print(SiralanmisDizi[i],end = ",")
