# Nama: Rozan Ghosani
# NIM : 16521411

# Program GambarBelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarBelahKetupat(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan lebar sebesar N sesuai spesifikasi soal
# KAMUS LOKAL
# N, i : int
# ALGORITMA
    for i in range(N):
        if i <= N // 2:
            print((N // 2 - i)*' ' + (2 * i + 1)*'*')
        else:
            print((i - N // 2)*' ' + (2 * (N - i) - 1)*'*')
    

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
    GambarBelahKetupat(N)
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")