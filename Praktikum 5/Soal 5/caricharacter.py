# Program CariCharacter
# Membaca sebuah integer positif N. Nilai N harus divalidasi sampai didapatkan nilai N yang benar, yaitu 0 < N <= 100.
# Selanjutnya, program menerima masukan sebuah character, misalnya CC, dan menghasilkan karakter pertama besar/kecil/non-huruf

# KAMUS
# N : int
# arr : array [0..N-1] of char
# flag : bool
# cc : char

# ALGORITMA
N = int(input())
while N <= 0 or N > 100: print('Masukan salah. Ulangi!'); N = int(input())

arr = ['' for i in range(N)]
for i in range(N): arr[i] = input()[0]

cc = input()[0]

if cc == 'L' or cc == 'l':
    flag = False
    for i in range(N):
        if 65 <= ord(arr[i]) <= 90:
            flag = True
            print(i + 1, arr[i])
            break
    if not flag: print('Tidak ada huruf besar')
elif cc == 'S' or cc == 's':
    flag = False
    for i in range(N):
        if 97 <= ord(arr[i]) <= 122:
            flag = True
            print(i + 1, arr[i])
            break
    if not flag: print('Tidak ada huruf kecil')            
elif cc == 'X' or cc == 'x':
    flag = False
    for i in range(N):
        if ord(arr[i]) < 65 or 90 < ord(arr[i]) < 97 or ord(arr[i]) > 122:
            flag = True
            print(i + 1, arr[i])
            break
    if not flag: print('Semua huruf')  
else: print('Tidak diproses')