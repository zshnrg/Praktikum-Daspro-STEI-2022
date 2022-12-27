module PersamaanKuadrat where

-- PERSAMAAN KUADRAT                persamaanKuadrat(a,b,c,x)

-- DEFINISI DAN SPESIFIKASI
persamaanKuadrat:: Int -> Int -> Int -> Int -> Int
{- Menghitung hasil persamaan kuadrat ax^2 + bx + c -}

-- REALISASI
persamaanKuadrat a b c x = a * x ^ 2 + b * x + c

-- APLIKASI
-- persamaanKuadrat 1 2 1 (-1)
