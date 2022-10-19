# Program Penduduk
# membaca masukan jumlah penduduk desa dari sebuah kecamatan di suatu kota
# menghitung jumlah penduduk kecamatan (total penduduk desa).

#  KAMUS
# N, Sum = int

# ALGORITMA
N = int(input())
Sum = 0

for i in range(N):
    Sum += int(input())

print(Sum)