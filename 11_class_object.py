class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobil1 = Mobil("Toyota", "Hitam")
mobil2 = Mobil("Honda", "Putih")
mobil1.info()
mobil2.info()
