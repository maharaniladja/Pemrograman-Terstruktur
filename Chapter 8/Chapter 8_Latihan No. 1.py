data = []
loop = 0

while loop < 4:
    bilangan = int(input("Masukkan bilangan bulat : "))
    data.append(bilangan)
    loop += 1

data.sort(reverse=True)
print("Data dari yang terbesar hingga terkecil adalah ", data)
