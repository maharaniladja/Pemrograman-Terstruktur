def rataratabuah(databuah):
    tupleData = tuple(databuah.values())
    tambah = sum(tupleData)
    hitung = len(tupleData)
    return tambah/hitung

buah = {'Apel': 5000, 'Jeruk': 8500, 'Mangga': 7800, 'Duku': 6500}
hasil = rataratabuah(buah)
if(hasil):
    print("Rata-rata keseluruhan data buah adalah ", hasil)
