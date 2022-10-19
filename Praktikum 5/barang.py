# Program Barang
# membaca input N yang merupakan jumlah barang. N diasumsikan selalu valid (N>0).
# Selanjutnya, program akan meminta input harga barang sebanyak N (input harga
# dianggap selalu valid) dan menghitung jumlah harga barang.

# KAMUS
# N, Sum = int

# ALGORITMA
N = int(input())
Sum = 0

for i in range(N):
    Sum += int(input())

print(Sum)