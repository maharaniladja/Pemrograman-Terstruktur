def sortStringByChar(myData):
    myData.sort(reverse=True, key=len)
    return(myData)

def listnamabuah():
    data = []
    loop = 0
    while loop < 4:
        namabuah = (input("Masukkan nama buah : "))
        data.append(namabuah)
        loop += 1
    return data

datalist = listnamabuah()
if(datalist):
    print("Hasil dari list buah : ", datalist)
    result = sortStringByChar(datalist)
    print(result)
