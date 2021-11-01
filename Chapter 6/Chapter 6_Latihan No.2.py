import math

#FORMASI BINTANG 1
print('----Formasi Bintang Pertama----')
def starFormation1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()
starFormation1(4)

#FORMASI BINTANG 2
print('-----Formasi Bintang Kedua-----')

def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()
starFormation2(4)

#FORMASI BINTANG 3
print('----Formasi Bintang Ketiga----')
n = 7
starFormation1(n//2+1)
starFormation2(n//2)


