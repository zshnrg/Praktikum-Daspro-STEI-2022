# Program KonversiSuhu
# mengkonversi suhu dari satuan Celcius ke satuan suhu yang lain, yaitu Fahrenheit, Reamur, atau Kelvin.

# KAMUS
# k : char
# C = float

# ALGORITMA
C = float(input())
k = input()[0]

if k == 'R':
    print('{:.02f}'.format(4/5 * C))
elif k == 'F':
    print('{:.02f}'.format((9/5 * C) + 32))
else:
    print('{:.02f}'.format(C + 273.15))