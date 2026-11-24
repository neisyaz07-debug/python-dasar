def bagi_angka(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi angka dengan nol!")
    except TypeError:
        print("Error: Input harus berupa angka!")
    else:
        print(f"Hasil pembagian {a} / {b} = {hasil}")
    finally:
        print("Proses pengecekan selesai.\n")

bagi_angka(10, 2)
bagi_angka(10, 0)
