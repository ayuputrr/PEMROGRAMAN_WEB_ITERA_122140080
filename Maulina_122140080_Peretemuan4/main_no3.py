
import mtk as mo

def tampilkan_menu():
    print("\n=== KALKULATOR MATEMATIKA BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Belah Ketupat")
    print("5. Segitiga")
    print("0. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih bangun datar (1-5 / 0 untuk keluar): ")

    if pilihan == "1":
        print("\n== PERSEGI ==")
        sisi = float(input("Masukkan sisi: "))
        print(f"Luas: {mo.luas_persegi(sisi)}")
        print(f"Keliling: {mo.keliling_persegi(sisi)}")

    elif pilihan == "2":
        print("\n== PERSEGI PANJANG ==")
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Luas: {mo.luas_persegi_panjang(panjang, lebar)}")
        print(f"Keliling: {mo.keliling_persegi_panjang(panjang, lebar)}")

    elif pilihan == "3":
        print("\n== LINGKARAN ==")
        r = float(input("Masukkan jari-jari: "))
        print(f"Luas: {mo.luas_lingkaran(r):.2f}")
        print(f"Keliling: {mo.keliling_lingkaran(r):.2f}")

    elif pilihan == "4":
        print("\n== BELAH KETUPAT ==")
        d1 = float(input("Masukkan diagonal 1: "))
        d2 = float(input("Masukkan diagonal 2: "))
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Luas: {mo.luas_belah_ketupat(d1, d2):.2f}")
        print(f"Keliling: {mo.keliling_belah_ketupat(sisi):.2f}")

    elif pilihan == "5":
        print("\n== SEGITIGA ==")
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        a = float(input("Masukkan sisi a: "))
        b = float(input("Masukkan sisi b: "))
        c = float(input("Masukkan sisi c: "))
        print(f"Luas: {mo.luas_segitiga(alas, tinggi):.2f}")
        print(f"Keliling: {mo.keliling_segitiga(a, b, c):.2f}")

    elif pilihan == "0":
        print("Terima kasih telah menggunakan kalkulator ini!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
