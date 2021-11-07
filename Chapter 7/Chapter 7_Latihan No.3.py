print('--------------------------')
print(' PROGRAM HITUNG RATA-RATA ')
print('--------------------------')

while True:
    try:
        bilangan = input("Masukkan bilangan bulat: ")
        bilanganbulat = [int(x) for x in bilangan]
        jumlah = 0
        for bilangan in bilanganbulat:
            jumlah += bilangan
            ratarata = jumlah/len(bilanganbulat)
            ulang = str(input("Mau lagi? (y/n) :"))
            if ulang == "y":
                print(end='')
            elif ulang == "n":
                print("Rata-ratanya adalah :", ratarata)
            break
        else:
            print("Data yang dimasukkan tidak valid")
            break
    except ValueError:
        print("Bukan bilangan bulat")
