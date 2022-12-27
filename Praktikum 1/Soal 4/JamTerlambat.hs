module JamTerlambat where

-- JAM TERLAMBAT                                           jamTerlambat(h,m,d)

-- DEFINISI DAN SPESIFIKASI
jamTerlambat :: Int -> Int -> Int -> (Int, Int, Int, Bool, Int)
{- Tuliskan fungsi jamTerlambat yang menerima input tiga buah bilangan integer
   yang merepresentasikan jam (0.23), menit (O..59), detik (0..59). Waktu mulai konser 08.30. 
   Fungsi mengembalikan selisih waktu, terlambat/tidak, kekecewaan penonton (selisih detik * 10) -}

-- REALISASI
jamTerlambat h m d =
    let jamMulaiToDetik = (8 * 3600) + (30 * 60)
        jamMasukToDetik = (h * 3600) + (m * 60) + d
        selisihDetik = if jamMulaiToDetik < jamMasukToDetik then jamMasukToDetik - jamMulaiToDetik
        else jamMulaiToDetik - jamMasukToDetik
    in (div selisihDetik 3600,
        div (mod selisihDetik 3600) 60,
        mod (mod selisihDetik 3600) 60,
        jamMulaiToDetik < jamMasukToDetik,
        if jamMulaiToDetik < jamMasukToDetik then selisihDetik*10 else 0)
