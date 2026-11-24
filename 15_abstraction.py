from abc import ABC, abstractmethod

# Abstract Class
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

persegi1 = Persegi(5)
print(f"Luas persegi dengan sisi {persegi1.sisi}: {persegi1.luas()}")
