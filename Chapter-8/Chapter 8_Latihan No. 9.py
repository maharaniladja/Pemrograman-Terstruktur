print("Pilihan dan Harga Buah :")
print("Apel   : 5000      Jeruk : 8500")
print("Mangga : 7800      Duku  : 6500")
print("==============================================")

buah = {'Apel': 5000, 'Jeruk': 8500, 'Mangga': 7800, 'Duku': 6500}
namabuah = input("Masukkan nama buah yang ingin dibeli : ")
jumlah = int(input("Berapa kg : "))
harga = int(buah[namabuah]) * jumlah
if namabuah in buah:
    print("Nama buah yang dibeli :", namabuah)
    print("Berapa kg             :", jumlah)
    print("---------------------------------")
    print("Total harga           :", harga)
else:
    print("Format yang dimasukkan salah")
