def asal_carpan(x):
    carpan_liste =[]
    for i in range(2, x):
        asal = True
        for j in range(2, i):
            if i % j == 0:
                asal = False

        if asal and x%i == 0:
            carpan_liste.append(i)

    return carpan_liste
sayi = int(raw_input("Bir sayi giriniz: "))
print asal_carpan(sayi)
