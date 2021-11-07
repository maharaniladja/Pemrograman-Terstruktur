#Program Python untuk membuka, membaca, dan kemudian menampilkan isi sebuah file text.

try:
    namafile = str(input("Masukkan nama file : "))
    file = open(f'D:/{namafile}.txt', "r")
    print("Isi file : ", file.read())
    
except FileNotFoundError:
    print('File tidak ditemukan')
