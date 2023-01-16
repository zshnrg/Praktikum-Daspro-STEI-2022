# Program: UkuranBaju
# mengotomatisasi penentuan ukuran baju panitia dengan memanfaatkan tinggi dalam cm (integer positif) dan berat badan dalam kg (integer positif)

# KAMUS
# t, b : int

# ALGORITMA
t = int(input())
b = int(input())

if t <= 150:
    print('1')
elif t > 150 and t <= 170:
    if b <= 80:
        print('2')
    else:
        print('3')
elif t >= 170 and b > 60 and b <= 80:
    print('3')
else:
    print('4')