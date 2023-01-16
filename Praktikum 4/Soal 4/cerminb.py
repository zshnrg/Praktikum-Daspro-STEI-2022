# Nama: Rozan Ghosani
# NIM : 16521411

# Program GambarBTercermin
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar b tercermin sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarBTercermin(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar b tercermin dengan lebar sebesar N sesuai spesifikasi soal
# KAMUS LOKAL
# N, i : int
# ALGORITMA
    for i in range(N):
        if i <= N // 2:
            print((2 * i)*' ' + (N - 2 * i)*'*')
        else:
            print((2 * (N - i - 1))*' ' + (N - 2 * (N - i - 1))*'*')
    

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# KAMUS LOKAL
# N : int
# ALGORITMA
    if N > 0 and N % 2 == 1:
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if IsValid(N):
    GambarBTercermin(N)
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")