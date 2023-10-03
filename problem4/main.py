# tulis solusi code disini
class Ongkos_kirim() : 
    def __init__(self, panjang, lebar, tinggi, berat) :
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat
    
    def menghitung_volume(self):
        Dimensi =  round(self.panjang * self.lebar * self.tinggi)
        Harga = 5000
        if Dimensi >= 50 and self.berat >= 1 :
            print("Harga :  Rp.", "{:,}".format(round(Harga)))
        else :
            print("Dimensi dan Berat dibawah standar")
    

Ongkos = Ongkos_kirim(5,2,5,1)
Ongkos.menghitung_volume()

# Input : 
# 	Panjang = 5
# 	Lebar = 2
# 	Tinggi = 4
# 	Berat = 1 kg
# Output :
# 	Harga : Rp 5000