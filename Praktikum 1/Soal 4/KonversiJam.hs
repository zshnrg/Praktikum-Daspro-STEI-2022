module KonversiJam where

-- KONVERSI JAM                  konversiJam(j, m, d)

-- Definisi dan Spesifikasi
konversiJam :: Int -> Int -> Int -> (Bool,Int,Int,Int)
{- konversiJam(j,m,d) menerima input 3 integer yang merupakan waktu John terbangun 
   dalam format jam(O..23) menit(0..59) detik(0..59) dan mengembalikan apakah John
   sempat mengucapkan selamat ulang tahun/tidak dan waktu setempat (lebih lambat 7 jam) -}

-- Realisasi
konversiJam j m d =
    if j>=7
    then (False,j-7,m,d)
    else (True, 24-(7-j), m, d)