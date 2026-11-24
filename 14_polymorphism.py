class Burung:
    def suara(self):
        return "Cuit-cuit!"

class Anjing:
    def suara(self):
        return "Guk-guk!"

# Polymorphism: fungsi yang sama memanggil method berbeda sesuai objeknya
def bunyikan_hewan(hewan):
    print(hewan.suara())

bunyikan_hewan(Burung())
bunyikan_hewan(Anjing())
