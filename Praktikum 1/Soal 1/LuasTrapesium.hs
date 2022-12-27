module LuasTrapesium where

-- LUAS TRAPESIUM                       luasTrapesium(t,a,b)

-- DEFINISI DAN SPESIFIKASI
luasTrapesium :: Float -> Float -> Float -> Float 
{- Menghitung luas trapesium berdasarkan input tinggi (t) serta dua sisi yang sejajar (a dan b) -}

-- REALISASI
luasTrapesium t a b = t * (a + b)/2

-- APLIKASI
-- luasTrapesium 5 12 13
