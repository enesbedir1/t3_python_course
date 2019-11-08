sayi = int(raw_input("uc basamakli sayi giriniz: "))

b1 = sayi%10

b2 = sayi//10
b2 = b2%10

b3 = sayi//100

print "birler basamagi", b1
print "onlar basamagi", b2
print "yuzler basamagi", b3
