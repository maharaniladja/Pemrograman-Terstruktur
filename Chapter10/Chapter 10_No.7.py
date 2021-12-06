#membuka file
myFile = open('D:/tekspergeseran.txt', 'r')
teks = myFile.read()
listPergeseran = list(teks)

#output
n = int(input("Masukkan banyak pergeseran : "))

#ubah kembali teks pergeseran
teksAsli = ''
for huruf in listPergeseran:
    if huruf.isalpha():
        hurufAscii = ord(huruf)
        ubahTeks = 65 + ((hurufAscii % 65) - n) % 26
        teksAsli += chr(ubahTeks)
    elif huruf.isspace():
        teksAsli += ' '
          
print("Ubah Kembali Ke Teks Asli : ", teksAsli)

#menutup file
myFile.close()

#membuat file baru
filehasilubah = open('D:/ubahkembaliteksasli.txt', 'w')
filehasilubah.write(teksAsli)

#menutup file
filehasilubah.close()
