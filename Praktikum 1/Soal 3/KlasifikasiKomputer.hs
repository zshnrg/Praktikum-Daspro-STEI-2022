module KlasifikasiKomputer where

-- KLASIFIKASI KOMPUTER                 klasifikasi(c, g, h)

-- DEFINISI DAN SPESIFIKASI
klasifikasi :: Int -> Int -> Int -> Int
{- klasifikasi(c, g, h) menerima integer c (kemampuan CPU), g (kemampuan GPU), dan h (kemampuan harddisk) untuk diklasifikasikan
   - PU > 7, GPU > 7, dan harddisk > 7, maka kelompok 5.
   - Jika setidaknya satu kemampuan bernilai kurang dari sama dengan dari 7, maka kelompok 4
   - Jika CPU, GPU, dan harddisk ≤ 7, maka kelompok 3
   - Jika CPU atau GPU kurang dari 5, maka kelompok 2
   - Jika salah satu nilai < 2, maka kelompok 1 (tidak peduli dengan nilai kemampuan lainnya)
   Prioritas kelompok dari yang terkecil ke terbesar -}

-- REALISASI
klasifikasi c g h
    | (c < 2 || g < 2 || h < 2) = 1
    | (c < 5 || g < 5) = 2
    | (c <= 7 && g <= 7 && h <= 7) = 3
    | (c > 7 && g > 7 && h > 7) = 5
    | otherwise = 4
