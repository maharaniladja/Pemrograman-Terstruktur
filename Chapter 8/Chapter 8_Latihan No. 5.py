def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False

def listdariuser():
    data = []
    loop = 0
    while loop < 4:
        bilangan = int(input("Masukkan bilangan bulat: "))
        data.append(bilangan)
        loop += 1
    return data

datalist = listdariuser()
if(datalist):
    print("Hasil kuadratnya adalah : ")
    result = kuadrat(datalist)
    print(result)
    
