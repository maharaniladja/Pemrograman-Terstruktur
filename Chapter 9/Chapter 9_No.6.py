datanilai = [{'NIM': 'A01', 'Nama': 'AGUSTINA', 'MID': 50, 'UAS': 80},
            {'NIM': 'A02', 'Nama': 'BUDI', 'MID': 40, 'UAS': 90},
            {'NIM': 'A03', 'Nama': 'CHICHA', 'MID': 100, 'UAS': 50},
            {'NIM': 'A04', 'Nama': 'DONNA', 'MID': 20, 'UAS': 100},
            {'NIM': 'A05', 'Nama': 'FATIMAH', 'MID': 70, 'UAS': 100}]

print("===========================================================")
print("NIM     NAMA        N.MID     N.UAS    N.AKHIR      STATUS")
print("-----------------------------------------------------------")

#menghitung nilai akhir:
for datanilai in datanilai:
    print(datanilai['NIM'].ljust(7), end='')
    print(datanilai['Nama'].ljust(8), end='')
    print(str(datanilai['MID']).rjust(10), end='')
    print(str(datanilai['UAS']).rjust(10), end='')
    
    NilaiAkhir = (datanilai['MID'] + 2*datanilai['UAS']) // 3
    print(str(round(NilaiAkhir)).rjust(11), end='')

#status diperoleh jika: 
    if NilaiAkhir >= 60:
        print('LULUS'.rjust(12))
        
    elif NilaiAkhir < 60:
        print('TIDAK LULUS'.rjust(12))

print("===========================================================")
