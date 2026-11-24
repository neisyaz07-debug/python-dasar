# Parent Class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")

# Child Class mewarisi sifat Hewan
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeong: Meong!")

kucing1 = Kucing("Mochi")
kucing1.makan()
kucing1.bersuara()
