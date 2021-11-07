while True:
    try:
        angka = input("Masukkan bilangan bulat :")
        daftar_baru = [int(x) for x in angka]
        jumlah = 0
        for angka in daftar_baru:
            jumlah += angka
        ratarata = jumlah / len(daftar_baru)
        ulang = str(input("Mau lagi? (y/n) :"))
        if ulang == "y":
            print(end='')
        elif ulang == "n":
            print("Rata-ratanya adalah :", ratarata)
            break
        else:
            print("Data tidak valid")
            break
    except ValueError:
        print("Bukan bilangan bulat")
