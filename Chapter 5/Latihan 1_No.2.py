NilaiBahasaIndonesia = int(input("Masukkan Nilai Bahasa Indonesia : "))
NilaiIpa = int(input("Masukkan Nilai IPA :"))
NilaiMatematika = int(input("Masukkan Nilai Matematika : "))
if (NilaiMatematika > 70) and (NilaiIpa > 60) and (NilaiBahasaIndonesia > 60):
    print("Lulus")
elif (NilaiMatematika < 0) or (NilaiIpa < 0) or (NilaiBahasaIndonesia < 0):
    print("Maaf, input ada yang tidak valid")
else:
    print("Tidak Lulus")
