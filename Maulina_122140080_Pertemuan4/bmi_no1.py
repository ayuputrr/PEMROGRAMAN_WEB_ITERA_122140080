print("=== KALKULATOR SEHAT: PENGHITUNG BMI ===")

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm atau meter): "))


if tinggi > 10:
    tinggi = tinggi / 100  


bmi = berat / (tinggi ** 2)


if bmi < 18.5:
    kategori = "Berat badan kurang"
elif bmi < 25:
    kategori = "Berat badan normal"
elif bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

print("\n=== HASIL PERHITUNGAN ===")
print(f"\nBMI Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")
