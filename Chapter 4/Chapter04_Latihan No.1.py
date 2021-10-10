print("---Program Menghitung Uang Parkir Otomatis---")

jammasuk1 = int(input("Masukkan jam masuk = "))
menitmasuk1 = int(input("Masukkan menit masuk ="))
menitmasuk1 = menitmasuk1/60
totalmasuk = jammasuk1+menitmasuk1
jamkeluar2 = int(input("Masukkan jam keluar ="))
menitkeluar2 = int(input("Masukkan menit keluar ="))
menitkeluar2 = menitkeluar2/60
totalkeluar = jamkeluar2+menitkeluar2
payment = 200000
lama = (totalkeluar)-(totalmasuk)

print("Lama Parkir = ", lama, "jam")
if lama ==12:
    duabelas_jam_pertama=payment
    print("Biaya Parkir = Rp", duabelas_jam_pertama)
elif lama >12:
    biaya_selanjutnya = (lama-12)*10000+payment
    print("Biaya Parkir =  Rp", biaya_selanjutnya)
elif lama > 13:
    biaya_selanjutnya = (lama-12)*10000+payment
    print("Biaya Parkir =  Rp", biaya_selanjutnya)
