module LamaTidur where

-- LAMA TIDUR                               lamaTidur(j,m,d)

-- DEFINISI DAN SPESIFIKASI
lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)
{- lamaTidur(j,m,d) menerima input 3 integer yang merupakan jam
   (0..23), menit(0..59), detik(0..59) waktu mereka selesai
   mempersiapkan acara dan menghitung lama mereka bisa tidur.
   serta apakah mereka cukup tidur (>= 6 jam) -}

-- REALISASI
lamaTidur j m d =
    let detikAwal = j * 3600 + m * 60 + d
        selisihDetik = 
            if detikAwal < 5*3600 then (5*3600) - detikAwal
            else ((5+24)*3600) - detikAwal
    in (selisihDetik >= 6*3600, div selisihDetik 3600, div (mod selisihDetik 3600) 60, mod selisihDetik 60)
