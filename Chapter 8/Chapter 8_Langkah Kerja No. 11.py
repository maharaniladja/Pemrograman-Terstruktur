a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("Data awal a :", a)
print("Data awal b :", b)
print("="*60)

a.insert(3, 10)
b.insert(2, 15)
print("Hasil setelah disisipkan nilai 10 ke indeks 3", a)
print("Hasil setelah disisipkan nilai 15 ke indeks 2", b)
print("="*60)

a.append(4)
b.append(8)
print("Hasil list a setelah disisipkan angka 4", a)
print("Hasil list a setelah disisipkan angka 8", b)
print("="*60)

a.sort()
b.sort()
print("Hasil list a disorting secara ascending", a)
print("Hasil list b disorting secara ascending", b)
print("="*60)

c = a[:8]
d = b[2:10]
print("List c yang merupakan sublist dari a(indeks 0-7)", c)
print("List c yang merupakan sublist dari b(indeks 2-9)", d)
print("="*60)

e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
print('Hasil list e yang merupakan penjumlahan dari setiap elemen list c dan d', e)
e = tuple(e)
print('Hasil list e yang dijadikan tuple', e)
print('='*60)

min = min(e)
max = max(e)
sum = sum(e)

print("Hasil min dari tuple", min)
print("Hasil max dari tuple", max)
print("Hasil sum dari tuple", sum)
print("="*60)

myString = "Python adalah bahasa pemrograman yang menyenangkan"
myString = set(myString)

print("Variabel myString", myString)
print("Karakter huruf yang menyusun myString", myString)
print("="*60)

myStringSetList = list(myString)
print("Bentuk list myString", myStringSetList)
myStringSetList.sort()
print("Bentuk list myString setelah di sorting ascending", myStringSetList)
