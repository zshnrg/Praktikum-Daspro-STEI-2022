# Program: Resistor
# Menerima 3 (tiga) bilangan riil yang merepresentasikan  nilai resistor R1, R2, dan R3,
# berupa bilangan rill > 0, dan menghitung nilai resistansi total, tergantung dihubungkan
# secara serial atau paralel

# KAMUS
# R1, R2, R3 : float
# pilihan : string
# loop : bool

def Seri(a, b):
    # menghasilkan resultan dua resistor seri
    # KAMUS LOKAL
    # a, b : float
    # ALGORITMA
    return a+b

def Paralel(a,b):
    # menghasilkan resultan dua resistor paralel
    # KAMUS LOKAL
    # a, b, : float
    # ALGORITMA 
    return (a*b) / (a+b)

# ALGORITMA PROGRAM UTAMA
loop = True

while loop:
    R1 = float(input())
    R2 = float(input())
    R3 = float(input())

    pilihan = input()

    if R1 > 0 and R2 > 0 and R3 > 0:
        if pilihan == 'S' or pilihan == 's':
            print("{:.02f}".format(Seri(Seri(R1,R2), R3)))
            loop = False
        elif pilihan == 'P' or pilihan == 'p':
            print("{:.02f}".format(Paralel(Paralel(R1,R2),R3)))
            loop = False
        else:
            print('Masukan salah')
    else:
        print('Masukan salah')