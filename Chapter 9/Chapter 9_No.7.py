Mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("===========================================================")
print("NIM    NAMA MAHASISWA        TANGGAL LAHIR     TEMPAT LAHIR")
print("-----------------------------------------------------------")

#dataMahasiswa:

for dataMhs in Mhs:
    List = dataMhs.split(":")
    NIM = List[0]
    Nama = List[1]
    TanggalLahir = List[2]
    dataTanggalLahir = TanggalLahir.split('-')
    FormatTanggalLahir = "{0}/{1}/{2}".format(
        dataTanggalLahir[2], dataTanggalLahir[1], dataTanggalLahir[0])
    TempatLahir = List[3]

    print(NIM.ljust(7), end='')
    print(Nama.ljust(22), end='')
    print(FormatTanggalLahir.ljust(18), end='')
    print(TempatLahir.ljust(10))

print("-----------------------------------------------------------")
