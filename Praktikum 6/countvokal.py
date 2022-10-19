# Program HitungVokal
# Membaca masukan sejumlah karakter dan menyimpannya ke file data.txt
# Membaca isi file data.txt, menghitung dan menampilkan ada berapa
# banyak karakter huruf hidup dalam file

# KAMUS
mark = '.' # constant mark : character = '.'
# huruf : str
# i, count : int

def TulisTeks():
# Membaca kalimat (kumpulan karakter) diakhiri mark dari keyboard
# dan menyimpannya ke file data.txt
    # KAMUS LOKAL
    # f : SEQFILE of char
    # kalimat
    # ALGORITMA
    f = open("data.txt",'w')
    kalimat = input() # Baca sebuah kalimat dari keyboard
                      # diakhiri mark '.'
                      # Kalimat kosong hanya ada mark
    f.write(kalimat)  # Menuliskan kalimat ke file
    f.close()

def BacaTeks():
# Membaca file data.txt diakhiri mark dan menghitung banyak huruf
# vokal pada kalimat tersebut
    # KAMUS LOKAL
    # f : SEQFILE of char
    # kalimat : str
    # ALGORIMA
    kalimat = ''
    f = open("data.txt", "r")
    kalimat = f.readline()
    f.close
    return kalimat
    

# ALGORITMA PROGRAM UTAMA
vokal = ['A','a','I','i','U','u','E','e','O','o']

TulisTeks()
count = 0
for huruf in (BacaTeks()):
    for i in range(10):
        if huruf == vokal[i]:
            count += 1
print(count)
# lengkapi program utama