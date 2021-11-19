def datastat(x):
    if(isinstance(x, list)):
        tupleX = tuple(x)
        a = sum(tupleX) / len(tupleX)
        b = max(tupleX)
        c = min(tupleX)
        return[a, b, c]

def datadariuser():
    data = []
    loop = 0
    while loop < 4:
        bilangan = int(input("Masukkan bilangan bulat : "))
        data.append(bilangan)
        loop += 1
    return data

listdata = datadariuser()
if(listdata):
    hasildata = datastat(listdata)
    print("                                  ")
    print("Rata-ratanya adalah {0} : {1}" .format(listdata, hasildata[0]))
    print("Nilai tertingginya adalah {0} : {1} " .format(listdata, hasildata[1]))
    print("Nilai terendahnya adalah {0} : {1} " .format(listdata, hasildata[2]))
