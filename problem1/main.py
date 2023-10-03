# tulis solusi code disini
class Persegi():
    def __init__(self, sisi):
        self.sisi = sisi

    def Luas_persegi(self):
        LuasPersegi = self.sisi * self.sisi
        return LuasPersegi

    def Keliling_persegi(self) :
        Keliling = (4 * self.sisi)
        return Keliling
    
class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def Luas_segitiga(self):
        Luas_segitiga = 0.5 * self.alas * self.tinggi
        return round(Luas_segitiga)
    
    def Keliling_segitiga(self) :
        Menghitung_sisi = pow(self.alas, 2) + pow(self.tinggi, 2)
        SisiKetiga = pow(Menghitung_sisi, 0.5)
        Keliling = self.alas + self.tinggi + SisiKetiga
        return round(Keliling)

class Persegi_Panjang():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def Luas_persegiPanjang(self):
        Luas_persegiPanjang = self.panjang * self.lebar
        return Luas_persegiPanjang
    
    def Keliling_persegiPanjang(self) :
        Keliling = (2 * self.panjang) + (2 * self.lebar)
        return Keliling

Hitung_persegi = Persegi(4)
Hitung_segitiga = Segitiga(3,4)
Hitung_persegiPanjang  = Persegi_Panjang(7,8)

print("LUAS")
print(f"Persegi : {Hitung_persegi.Luas_persegi()}")
print(f"Segitiga : {Hitung_segitiga.Luas_segitiga()}")
print(f"Persegi Panjang : {Hitung_persegiPanjang.Luas_persegiPanjang()}")

print("KELILING")
print(f"Persegi : {Hitung_persegi.Keliling_persegi()}")
print(f"Segitiga : {Hitung_segitiga.Keliling_segitiga()}")
print(f"Persegi Panjang : {Hitung_persegiPanjang.Keliling_persegiPanjang()}")

# INPUT
#   Luas
# 	Persegi (4)
# 	Segitiga (3,4)
# 	Persegi Panjang (7,8)

# 	Keliling
# 	Persegi (4)
# 	Segitiga (3,4)
# 	Persegi Panjang (7,8)
