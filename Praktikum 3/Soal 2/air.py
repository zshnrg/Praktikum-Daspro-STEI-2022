# Program: Air
# Membaca sebuah nilai T, suatu bilangan integer yang menyatakan temperatur
# air dalam derajat celcius untuk kondisi tekanan 1 atm.  Program menuliskan
# apakah kondisi air tersebut tergantung kepada temperaturnya.

# KAMUS
# T : int

# ALGORITMA
T = int(input())

if T >= 100:
    if T == 100: print('ANTARA CAIR-GAS')
    else: print('GAS')
elif T >= 0:
    if T == 0: print('ANTARA PADAT-CAIR')
    else: print('CAIR')
else: print('PADAT')
