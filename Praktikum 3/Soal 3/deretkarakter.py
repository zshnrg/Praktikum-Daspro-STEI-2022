# Program: Deret Karakter
# Tuliskan program yang membaca sebuah karakter C dan sebuah integer N,
# kemudian menuliskan dalam satu baris, karakter C sebanyak N. Asumsikan N > 0.

# KAMUS
# C = string
# N = int
# i = int

# ALGORITMA

C = str(input())[0]
N = int(input())

for i in range(N):
    print(C,end='')
print()