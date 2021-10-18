print("Hai.. nama saya Mr. Marky, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")

import random

angka = random.randint(0, 100)
tebakan = 0
score = 100
while tebakan != angka:

    tebakan = eval(input("Masukkan Angka Tebakan Anda :"))

    if tebakan == angka:
        print("Yeeey… Bilangan tebakan anda BENAR! ", tebakan)
    elif tebakan > angka:
        print("Bilangan Tebakan Anda Terlalu Besar")
    else:
        print("Bilangan Tebakan Anda Terlalu Kecil")
