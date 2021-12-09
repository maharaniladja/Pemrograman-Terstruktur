#program untuk menyimpan data peminjaman buku perpustakaan

from datetime import*

#membuat file
File = open('D:/DataPeminjamanBuku.txt', 'a')

#menginput data
while True:
    NIM = input('Masukkan NIM        : ')
    Nama = input('Masukkan Nama       : ')
    JdlBuku = input('Masukkan Judul Buku : ')
    now = datetime.date(datetime.now())
    awalpinjam = str(str(now.year) + '-' + str(now.month) + '-' + str(now.day))
    peminjaman = str(now + timedelta(days=7))

    String = NIM+'|'+Nama+'|'+JdlBuku+'|'+awalpinjam+'|'+peminjaman+'\n'
    File.write(String)

#mengulang perintah
    X = input('Ulangi lagi? (y/n)  : ')

    if X in ('n', 'N'):
        break
    
#menutup file
File.close()
    
    
