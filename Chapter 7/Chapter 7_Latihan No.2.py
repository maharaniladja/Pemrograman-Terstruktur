#Program Python untuk membuka, dan menambahkan data ke dalam sebuah file text

try:
    namafile = str(input("Masukkan nama file : "))
    file = open(f'D:/{namafile}.txt', "a")

except FileNotFoundError:
    print('File tidak ditemukan')

while True:
    
    tambahkandata = str(input("Data yang ingin ditambahkan : "))
    isifile = file.write(tambahkandata)
    ulang = str(input("Lagi? (y/n) : "))
    if ulang == "y":
        print(end='')
    elif ulang == "n":
        file.close()
        break
    else:
        print("Data tidak valid")
        break


