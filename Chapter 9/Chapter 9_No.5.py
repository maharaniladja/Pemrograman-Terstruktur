data = [{'NIM': 'A01', 'Nama': 'AGUSTINA', 'MID': 50, 'UAS': 80},
        {'NIM': 'A02', 'Nama': 'BUDI', 'MID': 40, 'UAS': 90},
        {'NIM': 'A03', 'Nama': 'CHICHA', 'MID': 100, 'UAS': 50},
        {'NIM': 'A04', 'Nama': 'DONNA', 'MID': 20, 'UAS': 100},
        {'NIM': 'A05', 'Nama': 'FATIMAH', 'MID': 70, 'UAS': 100}]

print("==========================================")
print("NIM    NamaMHS     Nilai MID    Nilai UAS")
print("------------------------------------------")

for i in range(len(data)):
    print(data[i]['NIM'].ljust(7), end='')
    print(data[i]['Nama'].ljust(8), end='')
    print(str(data[i]['MID']).rjust(10), end='')
    print(str(data[i]['UAS']).rjust(14))

print("------------------------------------------")
