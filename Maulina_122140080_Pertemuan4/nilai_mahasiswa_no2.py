

print("=== PROGRAM NILAI MAHASISWA ===\n")

jumlah = int(input("Masukkan jumlah mahasiswa: "))
mahasiswa = []


for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama     : ")
    nim = input("NIM      : ")
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    tugas = float(input("Nilai Tugas : "))

    nilai_akhir = 0.3 * uts + 0.4 * uas + 0.3 * tugas

    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "uts": uts,
        "uas": uas,
        "tugas": tugas,
        "nilai_akhir": nilai_akhir,
        "grade": grade
    })


print("\n=========== REKAP NILAI MAHASISWA ============")
print("{:<10} {:<10} {:<5} {:<5} {:<5} {:<12} {:<6}".format(
    "Nama", "NIM", "UTS", "UAS", "Tgs", "Nilai Akhir", "Grade"))
print("-" * 65)

for mhs in mahasiswa:
    print("{:<10} {:<10} {:<5} {:<5} {:<5} {:<12.2f} {:<6}".format(
        mhs["nama"], mhs["nim"], mhs["uts"], mhs["uas"], mhs["tugas"],
        mhs["nilai_akhir"], mhs["grade"]))


tertinggi = max(mahasiswa, key=lambda m: m["nilai_akhir"])
terendah = min(mahasiswa, key=lambda m: m["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{tertinggi['nama']} - {tertinggi['nilai_akhir']:.2f}")

print("Mahasiswa dengan nilai terendah:")
print(f"{terendah['nama']} - {terendah['nilai_akhir']:.2f}")

print("\n=== PROGRAM SELESAI ===")