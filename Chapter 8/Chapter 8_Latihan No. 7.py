def buahpalingmahal(databuah):
    listdatabuah = list(databuah.values())
    listdatabuah.sort(reverse=True)
    for x, y in databuah.items():
        if(listdatabuah[0] == y):
            return x
    return False

buah = {'Apel': 5000, 'Jeruk': 8500, 'Mangga': 7800, 'Duku': 6500}
hasil = buahpalingmahal(buah)
if(hasil):
    print("Buah yang paling mahal adalah : ", hasil)
