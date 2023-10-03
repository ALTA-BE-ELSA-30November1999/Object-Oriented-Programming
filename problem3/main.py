# tulis solusi code disini
class Kalkulator() : 
    def __init__(self, angka1, angka2) :
        self.angka1 = angka1
        self.angka2 = angka2
    
    def penjumlahan(self) :
        Jumlah = self.angka1 + self.angka2
        return Jumlah
    def pengurangan(self) :
        Kurang = self.angka1 - self.angka2
        return Kurang
    def Perkalian(self) :
        Kali = self.angka1 * self.angka2
        return Kali
    def pembagian(self) :
        Bagi = self.angka1 / self.angka2
        return int(Bagi)


Calculator = Kalkulator(3,4)
print(f"Penjumlahan : {Calculator.penjumlahan()}")
Calculator = Kalkulator(15,4)
print(f"Pengurangan : {Calculator.pengurangan()}")
Calculator = Kalkulator(10,10)
print(f"Perkalian : {Calculator.Perkalian()}")
Calculator = Kalkulator(12,3)
print(f"Pembagian : {Calculator.pembagian()}")


# Input : 
# 	Penjumlahan (3,4) 
# 	Pengurangan (15,4)
#   Perkalian (10,10)
# 	Pembagian (12,3)