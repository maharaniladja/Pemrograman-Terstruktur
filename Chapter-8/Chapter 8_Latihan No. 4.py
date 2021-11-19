print("============================================")
print("Data sayur : bayam, kangkung, wortel, selada")
print("============================================")
print("Menu : ")
print("A. Tambah Data Sayur")
print("B. Hapus Data Sayur")
print("C. Tampilkan Data Sayur")

datasayuran = ['bayam', 'kangkung', 'wortel', 'selada']
pilihdata = str(input("Masukkkan pilihan : "))

if pilihdata == "A":
    print("Pilihan anda adalah tambah data sayur")
    print("============================================")
    datasayuran.append(
        input("Masukkan nama sayur yang ingin ditambahkan : "))
    print("Data saat ini :", datasayuran)
    
elif pilihdata == "B":
    try:
        print("Pilihan anda adalah hapus data sayur")
        print("============================================")
        datasayuran.remove(
            input("Masukkan nama sayur yang ingin dihapus : "))
        print("Data sekarang :", datasayuran)
    except ValueError:
        print("Data tidak ditemukan")
        
elif pilihdata == "C":
    print("Pilihan anda adalah tampilkan data sayur")
    print("============================================")
    print("Data sayur saat ini : ", datasayuran)
