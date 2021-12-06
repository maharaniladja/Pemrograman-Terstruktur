#program Python untuk membaca data sebuah file text berisi serangkaian bilangan 

#membuka file
myFile = open("D:/filebilangan.txt", "r")

#menginput data
teks = ""
for data in myFile:
    filebilangan = data.split("|")
    filebilangan = filebilangan
    hasilbilangan = int(filebilangan[0]) + int(filebilangan[1].rstrip("\n"))
    teks += str(hasilbilangan) + "\n"

#membuat file hasil    
filehasil = open("D:/hasilbilangan.txt", "x")
filehasil.write(teks)

#menutup file
filehasil.close()
