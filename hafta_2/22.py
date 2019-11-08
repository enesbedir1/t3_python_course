sayi = int(raw_input("Sayi Giriniz:"))
toplam=0
for i in range(1,sayi):
    if(sayi%i == 0):
        print i
        toplam +=i

if(sayi == toplam):
    print("Mukemmel Sayidir.")
else:
    print("Mukemmel Sayi Degildir")
