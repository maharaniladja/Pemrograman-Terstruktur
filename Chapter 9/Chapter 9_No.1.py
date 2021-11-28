#ubah MATEMATIKA menjadi MASEMASIKA

teks = 'MATEMATIKA'

def ubahHuruf(teks, a, b):
    hurufBaru = teks.replace(a,b)
    print("Dari MATEMATIKA menjadi : ", hurufBaru)

ubahHuruf(teks, 'T', 'S')
