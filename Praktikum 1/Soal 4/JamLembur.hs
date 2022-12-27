module JamLembur where

-- JAM LEMBUR                                   jamLembur(j,m,d)

-- DEFINISI DAN SPESIFIKASI
jamLembur :: Int -> Int -> Int -> (Bool, Int, Int, Int)
{- jamLembur(j,m,d) menerima input tiga buah bilangan integer yang merepresentasikan
   jam (0..23), menit (0..59) dan detik (0..59). Ketiga input tersebut menunjukkan jam
   pulang dari kru konser. Jam pulang kru konser yang resmi adalah jam 16:30:00. 
   Menampilkan lembur/tidak, dan selisih dengan jam resmi. -}

-- REALISASI
jamLembur j m d =
    let 
        selisihDetik j m d = abs( ((j*3600) + (m*60) + d) - ((16 * 3600) + (30 * 60)) )
    in
        if (j >= 16 && m >= 30 && d > 0) || (j > 16) then (True,div (selisihDetik j m d) 3600, div (mod (selisihDetik j m d) 3600) 60, mod (selisihDetik j m d) 60)
        else (False,div (selisihDetik j m d) 3600, div (mod (selisihDetik j m d) 3600) 60, mod (selisihDetik j m d) 60)
