import statistics

#Bagian A
def jumlah(*myData):
    sum = +0

    for data in myData:
        sum += data

    jumlah1 = sum
    print('Jumlah :', jumlah1)

jumlah(5, 10, 4, 9, 30, 16, 2, 11)
jumlah(81, 98, 12, 83, 45, 77, 69, 30, 56)


#Bagian B
def avarage(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data
        i += 1

    avarage1 = sum/i
    print('Avarage :', avarage1)

avarage(5, 10, 4, 9, 30, 16, 2, 11)
avarage(81, 98, 12, 83, 45, 77, 69, 30, 56)


#Bagian C
def maksimal(*myData):

    for data in myData:
        max(myData) == data

    maksimal1 = max(myData)
    print('Nilai Maksimal :', maksimal1)

maksimal(5, 10, 4, 9, 30, 16, 2, 11)
maksimal(81, 98, 12, 83, 45, 77, 69, 30, 56)


#Bagian D
def minimum(*myData):

    for data in myData:
        min(myData) == data

    minimum1 = min(myData)
    print('Nilai Minimum :', minimum1)

minimum(5, 10, 4, 9, 30, 16, 2, 11)
minimum(81, 98, 12, 83, 45, 77, 69, 30, 56)
