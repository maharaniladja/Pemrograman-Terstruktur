#masukkan teks
teksawal = "SAYA SUKA PYTHON"
listPergeseran = list(teksawal)

#output
n = int(input("Masukkan banyak pergeseran : "))

#menginput hasil pergeseran
teksSandi = ''
for huruf in listPergeseran:
    if huruf.isalpha():
        hurufAscii = ord(huruf)
        hasilPergeseran = 65 + ((hurufAscii % 65) + n) % 26
        teksSandi += chr(hasilPergeseran)
    elif huruf.isspace():
        hasilPergeseran = chr(32)
        teksSandi += ' '
          
#output
print("Hasil Pergeseran : ", teksSandi)

#membuat dan membuka file
filehasil = open('D:/HasilPergeseran.txt', 'w')
filehasil.write(teksSandi)

#menutup file
filehasil.close()
