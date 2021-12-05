myfile = open("D:/datano1.txt", "r")
genap = 0
ganjil = 0

for data in myfile:
    if (int(data) % 2 == 0):
        ganjil += 1
    else:
        genap += 1
    
print("Banyak bilangan genap : ", genap)
print("Banyak bilangan ganjil : ", ganjil)

