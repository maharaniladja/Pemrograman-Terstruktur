#membuka file
myFile = open("D:/dataMahasiswa.txt", "a")

#menginput data
while True:
    NIM = input("Masukkan NIM    : ")
    Nama = input("Masukkan Nama   : ")
    Alamat = input("Masukkan Alamat : ")

    myString = NIM+"|"+Nama+"|"+Alamat+"\n"
    myFile.write(myString)

    X = input("Ulangi input? (y/n) : ")

    if X in ("N", "n"):
        break

#menutup file   
myFile.close()
