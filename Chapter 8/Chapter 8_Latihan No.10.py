print("Pilihan dan Harga Buah :")
print("Apel   : 5000      Jeruk : 8500")
print("Mangga : 7800      Duku  : 6500")
print("==============================================")

buah = {'Apel': 5000, 'Jeruk': 8500, 'Mangga': 7800, 'Duku': 6500}
total = 0
while True:
    namabuah = input("Masukkan nama buah yang ingin dibeli : ")
    jumlah = int(input("Berapa kg : "))
    total += (buah[namabuah] * jumlah)
    if namabuah in buah:
        print("---------------------------------------")
        print("Nama buah yang dibeli : ", namabuah)
        print("Berapa kg             : ", jumlah)
    ulang = str(input("Beli buah yang lain? (y/n) : "))
    print("---------------------------------------")
    if ulang == "y":
        print(end='')
    elif ulang == "n":
        print("Total harga           : ", total)
        break
