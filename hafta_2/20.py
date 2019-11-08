n = int(raw_input("Baslangic degeri: "))
while n > 1:
    if n % 2 == 0:  # n cift sayiysa
        n = n/2
    else:   # n tek sayiysa
        n = 3*n + 1
    print int(n)
