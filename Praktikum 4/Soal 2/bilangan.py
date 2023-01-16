# Program: Bilangan
# Membaca sebuah integer positif N. Nilai N harus divalidasi sampai didapatkan nilai N yang benar, yaitu 0 < N <= 100.
# Selanjutnya, program menerima masukan sebuah integer, misalnya X, dan menghasilkan:
# Jika X = 0, tuliskan urutan pertama ditemukannya bilangan 0. Jika tidak ada bilangan 0, tuliskan “Tidak ada 0”.
# Jika X = -1, maka tuliskan urutan pertama ditemukannya bilangan negatif dan tuliskan bilangannya. Jika tidak ada bilangan negatif, tuliskan “Tidak ada negatif”.
# Jika X = 1, maka tuliskan urutan pertama ditemukannya bilangan positif dan tuliskan bilangannya. Jika tidak ada bilangan positif, tuliskan “Tidak ada positif”.
# Jika X selain -1..1, tuliskan: “Tidak diproses”.

# KAMUS
# N : int
# B : array [0..N-1] of int
# i, x : int
# flag : bool

# ALGORITMA

# Meminta masukan N
N = int(input())
while N <= 0 or N > 100:
    print('Masukan salah. Ulangi!')
    N = int(input())

# Membuat array B
B = [0 for i in range(N)]

# Mengisi array B
for i in range(N):
    B[i] = int(input())

x = int(input())
flag = False

if x == 0:
    for i in range(N):
        if B[i] == 0:
            print(i+1)
            flag = True
            break
    if flag == False:
        print('Tidak ada 0')
elif x == 1:
    for i in range(N):
        if B[i] > 0:
            print(i+1, B[i])
            flag = True
            break
    if flag == False:
        print('Tidak ada positif')
elif x == -1:
    for i in range(N):
        if B[i] < 0:
            print(i+1, B[i])
            flag = True
            break
    if flag == False:
        print('Tidak ada negatif')
else:
    print('Tidak diproses')