#program Python untuk mencari data peminjaman buku berdasarkan kode member

from datetime import*

#membuka file
File = open('D:/DataPeminjamanBuku.txt', 'r')
search = input('Masukkan Kode Member : ')

#menginput data
def late(y):
    now = datetime.date(datetime.now())
    date = datetime.strptime(y, '%Y-%m-%d').date()
    return int((date-now).days)

result = False
for data in File:
    datapeminjaman = data.split('|').copy()
    code = data.split('|')[0]
    if (code == search):
        result = datapeminjaman
        break
    
if(result):
    makspeminjaman = datapeminjaman[4].rstrip('\n')
    late = late(makspeminjaman)
    if(late <= 0):
        text = '-'
        denda = '-'
    elif (late > 0):
        text = str(late) + 'hari'
        denda = 'Rp ' + str(late*2000)

#untuk output
print('-------------------------------------------------')
print('                 Data Mahasiswa                  ')
print('-------------------------------------------------')
print('Kode Member                 :', datapeminjaman[0])
print('Nama Member                 :', datapeminjaman[1])
print('Nama Buku                   :', datapeminjaman[2])
print('Tanggal Mulai Peminjaman    :', datapeminjaman[3])
print('Tanggal Maksimal Peminjaman :', makspeminjaman)
print('Tanggal Pengembalian        :', datetime.date(datetime.now()))
print('Terlambat                   :', text)
print('Denda                       :', denda)
print('-------------------------------------------------')      

    
