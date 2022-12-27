module KonversiSuhu where

-- KONVERSI SUHU            konversiSuhu(t, k)

-- DEFINISI DAN SPESIFIKASI
konversiSuhu :: Float -> Char -> Float

-- REALISASI
konversiSuhu t k 
    | k == 'R' = 4/5 * t
    | k == 'F' = (9/5 * t) + 32
    | k == 'K' = t + 273.15

-- APLIKASI
-- konversiSuhu 25 ‘R’
