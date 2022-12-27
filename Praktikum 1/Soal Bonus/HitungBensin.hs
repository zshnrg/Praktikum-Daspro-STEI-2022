module HitungBensin where

-- HITUNG BENSIN                                       hitungBensin(a,b)

hitungBensin :: Int -> Int -> Int
{- hitungBensin(a,b) menerima 2 buah bilangan bulat, A dan B (A <= B).
   Fungsi ini kemudian mengeluarkan sebuah bilangan bulat yang
   menunjukkan konsumsi bensin dari tiap-tiap kendaraan dari A sampai B
   -}
hitungPosisi :: Int -> Int
{- hitungPosisi(a) menerima posisi bilangan bulat positif. Jika a adalah
   bilangan genap, kendaraan tersebut akan bergerak ke titik a/2. Jika a
   adalah bilangan ganjil, kendaraan tersebut akan bergerak ke posisi
   (3a + 1). Hal ini terus dilakukan sampai kendaraan tersebut sampai ke
   kantor pusat yang terletak pada posisi 1. -}

-- REALISASI
hitungBensin a b =
    if a > b then 0
    else hitungPosisi(a) + (hitungBensin (a+1) b)

hitungPosisi a =
    if a == 1 then 0
    else if mod a 2 == 0 then 1 + hitungPosisi(div a 2)
    else 1 + hitungPosisi(3*a + 1)