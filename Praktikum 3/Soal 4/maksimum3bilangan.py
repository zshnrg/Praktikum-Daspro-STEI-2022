# Program: Maksimum 3 Bilangan
# Tuliskanlah sebuah program yang membaca 3 buah bilangan integer dan menuliskan nilai terbesar di antara ketiganya.

# KAMUS
# N1 : int
# N2 : int
# N3 : int
# max : int

# ALGORITMA
N1 = int(input())
N2 = int(input())
N3 = int(input())

if N1 >= N2 and N1 >= N3: print(N1)
elif N2 >= N1 and N2 >= N3: print(N2)
else: print(N3)