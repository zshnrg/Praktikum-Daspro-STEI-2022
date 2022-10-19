# Nama: Rozan Ghosani
# NIM : 16521411

# Program GambarPita
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar pita sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarPita(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar pita dengan lebar sebesar N sesuai spesifikasi soal
# KAMUS LOKAL
# N, i : int
# ALGORITMA
    for i in range(N):
        if i <= N // 2:
            print(i*' ' + (N-2*i)*'*')
        else:
            print((N-i-1)*' ' + (2*(i-(N//2))+1)*'*')
    

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
    GambarPita(N)
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")