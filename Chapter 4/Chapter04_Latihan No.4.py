# Menghitung jarak A ke B dan B ke C
jarakAkeB = float(input("Masukkan jarak A ke B :"))
rataratakecepatanAkeB = float(input("Masukkan rata-rata kecepatan:"))
waktutempuhAkeB = jarakAkeB/rataratakecepatanAkeB
print("Waktu tempuh adalah :", round(jarakAkeB//rataratakecepatanAkeB), "jam",
      round((jarakAkeB/rataratakecepatanAkeB-jarakAkeB//rataratakecepatanAkeB)*60), "Menit")

jarakBkeC = float(input("Masukkan jarak B ke C :"))
rataratakecepatanBkeC = float(input("Masukkan rata-rata kecepatan:"))
waktutempuhBkeC = jarakBkeC/rataratakecepatanBkeC
print("Waktu tempuh adalah :", round(jarakBkeC//rataratakecepatanBkeC), "jam",
      round((jarakBkeC/rataratakecepatanBkeC-jarakBkeC//rataratakecepatanBkeC)*60), "Menit")

# Jam sampai di C setelah ada istirahat 45 menit di B
jamberangkat = int(input("Masukkan jam berangkat = "))
menitberangkat = int(input("Masukkan menit berangkat ="))
menitberangkat = menitberangkat/60
jamsampaiAmenujuC = int(11)
menitsampaiAmenujuC = 60
print("Input jam istirahat di B")
jamistirahat = int(input("Masukkan jam istirahat ="))
menitistirahat = int(input("Masukkan menit istirahat ="))
print("Jam sampai di C", int(jamistirahat+1 + jamsampaiAmenujuC))
print("Menit sampai di C", int(menitsampaiAmenujuC+20-menitistirahat))
