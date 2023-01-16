# Program Segitiga
# menghitung luas segitiga.

# KAMUS
# masukan : string
# alas, tinggi : int

# ALGORITMA
masukan = input()
for i in range(len(masukan)):
    if masukan[i] == ' ':
        alas = int(masukan[:i])
        tinggi = int(masukan[i+1:])

if alas <= 0 or tinggi <= 0: print('Alas dan tinggi harus > 0')
else: print(round(alas*tinggi/2))