module LuasLayang where

-- LUAS LAYANG-LAYANG                           layang(d1,d2)

-- DEFINISI DAN SPESIFIKASI
layang :: Int -> Int -> Float
{- Menghitung luas layang-layang berdasarkan diagonal 1 dan diagonal 2 -}

-- REALISASI
layang d1 d2 = 0.5 * fromIntegral (d1 * d2)

-- APLIKASI
-- layang 3 7
