n = int(input('Masukan Nilai : '))
count = 0

for i in range(1, n):
    if i % 2 == 1:
        print(i)

        count = count + 1
print()
print()
print('Banyak bilangan ganjil : %d buah' % count)
