berat = int(input())

count_mhs = count_upper = count_lower = Sum = 0
while (berat != -999):
    if 30 <= berat <= 200:
        count_mhs += 1
        Sum += berat
        if berat >= 100: count_upper += 1
        elif berat <= 50: count_lower += 1
    berat = int(input())

if (count_mhs != 0):
    print(count_mhs)
    print(count_upper)
    print(count_lower)
    rata = Sum/count_mhs
    if (round(rata,1) * 10) % 10 == 5: print(int(rata + 0.5)) # rounding python aneh
    else: print(round(Sum / count_mhs))
else: print('Data kosong')