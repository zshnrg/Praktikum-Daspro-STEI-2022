module SumOfDigits where

-- JUMLAH SEMUA DIGIT                                   sumOfDigits(a)

-- DEFINISI DAN SPESIFIKASI
sumOfDigits :: Int -> Int
{- sumOfDigits(a) menghasilkan jumlah tiap digit dari
   a, sebuah integer positif, dengan menggunakan
   pendekatan rekursif dengan basis 0 -}

-- REALISASI
sumOfDigits a
    | a == 0 = 0                                         -- basis
    | otherwise = (mod a 10) + sumOfDigits (div a 10)    -- rekurens