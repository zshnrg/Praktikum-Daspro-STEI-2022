# Program: Beasiswa
# Buatlah program yang membaca input 2 buah bilangan riil (float),
# misalnya ip dan pot, dengan ip mewakili IP mahasiswa (bernilai 0..4)
# dan pot mewakili pendapatan orang tua (dalam juta rupiah, bernilai >= 0)
# dan menuliskan ke layar kategori beasiswa (bernilai 0..4) yang berhak
# didapatkan oleh mahasiswa tersebut

# KAMUS
# ip : float
# pot : float

# ALGORITMA
ip = float(input())
pot = float(input())

if ip >= 3.5:
    print('4')
elif ip < 3.5 and ip >= 0:
    if pot < 1:
        print('1')
    elif pot < 5:
        if ip >= 2:
            print('3')
        else:
            print('2')
    else:
        print('0')
else:
    print('0')