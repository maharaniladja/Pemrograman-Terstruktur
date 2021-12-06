#membuka file
myFile = open("D:/dataMahasiswa.txt", "r")

#mencari file
search = input("Masukkan NIM yang ingin dicari : ")

#menginput data
for data in myFile:
    dataFile = data.split("|").copy()
    NIM = data.split("|")[0]
    
    if NIM == search:
        print("Data Mahasiswa")
        print("NIM    : ", dataFile[0])
        print("Nama   : ", dataFile[1])
        print("Alamat : ", dataFile[2])

    else:
        ("Data mahasiswa yang dicari tidak ditemukan")

#menutup file
myFile.close()
