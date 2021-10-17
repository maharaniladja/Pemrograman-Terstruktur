NilaiBahasaIndonesia = int(input("Masukkan Nilai Bahasa Indonesia : "))
NilaiIpa = int(input("Masukkan Nilai IPA :"))
NilaiMatematika = int(input("Masukkan Nilai Matematika : "))
sebab1 = str(" Sebab : Nilai Matematika kurang dari 70")
sebab2 = str(" Sebab : Nilai Bahasa Indonesia kurang dari 60")
sebab3 = str(" Sebab : Nilai Ipa Kurang dari 60")

#statuskelulusan
if (NilaiMatematika < 0) or (NilaiIpa < 0) or (NilaiBahasaIndonesia < 0):
    print("Maaf, input ada yang tidak valid")
elif (NilaiMatematika < 70) or (NilaiIpa < 60) or (NilaiBahasaIndonesia < 60):
    print('Status Kelulusan : TIDAK LULUS')
else :
    print('Status Kelulusan : LULUS')

#sebab
if (NilaiMatematika < 70) or (NilaiIpa < 60) or (NilaiBahasaIndonesia < 60):
    print("Tidak Lulus")
if (NilaiMatematika < 70):
    print("Tidak Lulus" + sebab1)
if (NilaiIpa < 60):
    print("Tidak Lulus" + sebab2)
if (NilaiBahasaIndonesia < 60):
    print("Tidak Lulus" + sebab3)
