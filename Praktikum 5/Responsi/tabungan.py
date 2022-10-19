# Program Tabungan
# membaca masukan jumlah tabungan dari sejumlah siswa di suatu kelas dan menghitung jumlah tabungan.

# KAMUS
# N, Sum = int

# ALGORITMA
N = int(input())
Sum = 0

for i in range(N):
    Sum += int(input())

print(Sum)