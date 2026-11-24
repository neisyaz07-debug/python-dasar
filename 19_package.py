from toko_package.diskon import hitung_harga_akhir

harga_awal = 250000
diskon = 20
total = hitung_harga_akhir(harga_awal, diskon)

print(f"Harga awal: Rp{harga_awal:,}")
print(f"Setelah diskon {diskon}%: Rp{total:,.0f}")
