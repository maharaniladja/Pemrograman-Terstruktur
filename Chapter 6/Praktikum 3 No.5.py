def gabung(a, b, c, d):
    hasil = a + b * c - d
    return hasil

def gabung1(a, b, c, d):
    hasil = (a + b) * (c - d)
    return hasil

def gabung2(a, b, c, d, e, f):
    hasil = (a + b) / (c + d) / (e - f)
    return hasil

a = 2
b = 4
c = 6
d = 4
print(a, '+', b, '*', c, '-', d, '=', gabung(a, b, c, d))

a = 4
b = 7
c = 6
d = 9
print((a, '+', b), '*', (c, '-', d), '=', gabung1(a, b, c, d))


a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print((a, '+', b), '/', (c, '+', d), '/', (e, '-', f), '=', gabung2(a, b, c, d, e, f))
