import statistics

#Bagian A
def jumlah(*myData):
    sum = +0

    for data in myData:
        sum += data

    jumlah1 = sum
    print('Jumlah :', jumlah1)

#Bagian B
def avarage(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data
        i += 1

    avarage1 = sum/i
    print('Avarage :', avarage1)

#Bagian C
def maksimal(*myData):

    for data in myData:
        max(myData) == data

    maksimal1 = max(myData)
    print('Nilai Maksimal :', maksimal1)

#Bagian D
def minimum(*myData):

    for data in myData:
        min(myData) == data

    minimum1 = min(myData)
    print('Nilai Minimum :', minimum1)
