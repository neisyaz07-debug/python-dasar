class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal  # Private attribute

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def cek_saldo(self):
        return f"Saldo {self.pemilik}: Rp{self.__saldo:,}"

akun = RekeningBank("Neisya", 500000)
akun.setor(250000)
print(akun.cek_saldo())
