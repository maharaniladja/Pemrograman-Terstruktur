#membuka file
myfile = open("D:/datano1.txt", "r")

#nilai ganjil dan genap
genap = 0
ganjil = 0

#menginput data
for data in myfile:
    if (int(data) % 2 == 0):
        ganjil += 1
    else:
        genap += 1

#output   
print("Banyak bilangan genap : ", genap)
print("Banyak bilangan ganjil : ", ganjil)

