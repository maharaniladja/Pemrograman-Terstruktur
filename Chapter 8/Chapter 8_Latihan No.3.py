data = []
loop = 0

while loop < 4:
    namamahasiswa = input("Masukkan nama mahasiswa : ")
    data.append(namamahasiswa)
    loop += 1

data.sort()
for namamahasiswa in data:
    print("{0} ({1} karakter)".format(
        namamahasiswa, len(tuple(namamahasiswa))))
