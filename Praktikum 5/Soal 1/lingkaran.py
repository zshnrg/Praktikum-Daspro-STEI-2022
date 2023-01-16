# Program Lingkaran
# menghitung luas lingkaran.

# KAMUS
# r : int
# luas : float

# ALGORITMA
r = int(input())
if r <= 0: print('Jari-jari harus > 0')
else: print("%.2f" % float(3.1415 * r * r))