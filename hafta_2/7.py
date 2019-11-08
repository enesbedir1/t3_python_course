kullanici_adi = raw_input("Kullanici adi giriniz: ")
parola = raw_input("parola giriniz: ")

if kullanici_adi == "t3" and parola == "1453":
    print "Kullanici adi ve parola dogru!"
    print "Hosgeldin", kullanici_adi

elif kullanici_adi == "t3":
    print "parola yanlis!"

else:
    print "yanlis kullanici adi girdiniz!"
