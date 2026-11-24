nama_file = "catatan_praktikum.txt"

# Menulis ke dalam file (Write)
with open(nama_file, "w", encoding="utf-8") as file:
    file.write("Baris 1: Praktikum Python Dasar Santrikoding\n")
    file.write("Baris 2: Materi File Handling berhasil dijalankan.\n")

# Membaca isi file (Read)
with open(nama_file, "r", encoding="utf-8") as file:
    isi = file.read()
    print("=== Isi File ===")
    print(isi)
