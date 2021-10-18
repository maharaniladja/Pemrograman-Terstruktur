n = int(input('Masukan Nilai : '))
count = 0
summ = 0

for i in range(1, n):
    if i % 2 == 1:
        print(i)

        count = count + 1
        summ = summ + i
print()
print()
print('Banyak bilangan ganjil : %d buah' % count)
print('Jumlah seluruh bilangan : %d' % summ)
