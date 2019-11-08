x = int(raw_input("sayi giriniz: "))

for i in range(2,x):
    asal = True
    for j in range(2,i):
        if i%j==0:
            asal = False

    if asal:
        print i
