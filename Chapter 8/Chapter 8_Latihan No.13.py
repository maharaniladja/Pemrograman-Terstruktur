nilaiMhs = [{'NIM': 'A01', 'nama': 'Amir', 'MID': 50, 'UAS': 80},
            {'NIM': 'A02', 'nama': 'Budi', 'MID': 40, 'UAS': 90},
            {'NIM': 'A03', 'nama': 'Cici', 'MID': 50, 'UAS': 50},
            {'NIM': 'A04', 'nama': 'Dedi', 'MID': 20, 'UAS': 30},
            {'NIM': 'A05', 'nama': 'Fifi', 'MID': 70, 'UAS': 40}]

def menemukandatatertinggi(data):
    nilaiAkhir = None
    result = {}
    
    for x in data:
        nilai = (x['MID'] + (2 * x['UAS'])) / 3
        if(nilaiAkhir is None) or (nilai > nilaiAkhir):
            nilaiAkhir = nilai
            result['NIM'] = x['NIM']
            result['nama'] = x['nama']
    return result

result = menemukandatatertinggi(nilaiMhs)
if(bool(result)):
    print("Mahasiswa yang memiliki nilai tertinggi yaitu {0} dengan NIM {1}".format(
        result['nama'], result['NIM']))
