# Fungsi dengan parameter default dan return value
def hitung_diskon(harga, persen_diskon=10):
    potongan = harga * (persen_diskon / 100)
    return harga - potongan

total1 = hitung_diskon(100000)
total2 = hitung_diskon(200000, 25)

print(f"Harga setelah diskon default (10%): Rp{total1:,.0f}")
print(f"Harga setelah diskon khusus (25%): Rp{total2:,.0f}")
