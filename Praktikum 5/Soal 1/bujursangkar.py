# Program BujurSangkar
# menerima input sisi (dalam bentuk integer). Input sisi harus divalidasi sehingga
# selalu > 0. Apabila sisi yang dimasukkan <= 0, program akan mengeluarkan pesan error.
# Setelah sisi yang dimasukkan valid, program menghasilkan luas sisi dengan rumus: sisi * sisi

# KAMUS
# sisi : int

# ALGORITMA

sisi = int(input())

if sisi > 0: print(sisi*sisi)
else: print('Sisi harus > 0')