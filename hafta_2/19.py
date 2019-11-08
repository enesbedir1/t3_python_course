def fibo(x):
	a = 1
	b = 1
	for i in range(sayi):
		print a
		c = a + b
		a = b
		b = c

sayi = int(raw_input("Bir sayi giriniz: "))
fibo(sayi)
