meyve_liste = ["Elma","Armut","Portakal","visne"]

liste1 = [12.43, "Turkiye", "python", 1.0, 19]

print "liste1'in uzunlugu: ", len(liste1) # liste1 in uzunlugunu yazdirir.
print "liste1: ", liste1  # liste1 i yazdirir.

liste1.append("Bilim") #liste1 e "Bilim" adli elemanini ekler.

liste1.remove("python")  # "python" adli eleman listeden cikartirilir.

print "ekleme ve cikarmalardan sonra liste1: ", liste1

print "listenin 1. elemani", liste1[0]  # Listelerde sira sayisi 0'dan baslar
print "listenin 2. elemani", liste1[1]

liste1[0] = 12 # listenin ilk elemanini 12 yapti

print "liste1: ", liste1
