# mtk.py (math_operations.py)
# Modul operasi matematika sederhana

PI = 3.14159

# Fungsi geometri dasar
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_lingkaran(radius):
    return PI * radius * radius

def keliling_lingkaran(radius):
    return 2 * PI * radius

# Fungsi belah ketupat
def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def keliling_belah_ketupat(sisi):
    return 4 * sisi

# Fungsi segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c

# Fungsi konversi suhu
def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15
