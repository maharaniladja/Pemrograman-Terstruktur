print("Pilihan dan Harga Buah yang Ada :")
print("Apel   : 5000      Jeruk : 8500")
print("Mangga : 7800      Duku  : 6500")
print("==============================================")
print("Menu :")
print("A. Tambah Data Buah")
print("B. Beli Buah")
databuah = {'Apel': 5000, 'Jeruk': 8500, 'Mangga': 7800, 'Duku': 6500}
pilih = str(input("Masukkkan pilihan : "))
print("==============================================")

if pilih == "A":
    buahbaru = input("Masukkan nama buah  : ")
    if(buahbaru in databuah):
        print("Buah sudah ada")
    else:
        while True:
            hargabaru = int(input("Masukkan harga buah : "))
            databuah[buahbaru] = hargabaru
            print("Data buah saat ini : ", databuah)
            break
        
elif pilih == "B":
    total = 0
    while True:
        namabuah = input("Masukkan nama buah yang ingin dibeli : ")
        jumlah = int(input("Berapa kg : "))
        total += (databuah[namabuah] * jumlah)
        if namabuah in databuah:
            print("Nama buah yang dibeli :", namabuah)
            print("Berapa kg             :", jumlah)
        ulang = str(input("Beli buah yang lain? (y/n) : "))
        print("-------------------------------------------")
        if ulang == "y":
            print(end='')
        elif ulang == "n":
            print("Total harga           :", total)
            break
