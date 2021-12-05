#membuka file
myFile = open("D:/dataMahasiswa.txt", "r")

#membaca data
listdata = []
bacaData = myFile.readlines()

#memecah data
for i in range(len(bacaData)):
    pecahData = bacaData[i].split('|')
    dataDict = {"NIM" : pecahData[0], "Nama" : pecahData[1], "Alamat" : pecahData[2].replace("\n","")}
    listdata += [dataDict]

print('')
print("dataMahasiswa = ", listdata)

#menutup file
myFile.close()
