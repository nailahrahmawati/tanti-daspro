def gajiperminggu(gajibulan):
    return round (gajibulan / 4.45)

def gajiperhari(gajiperminggu, jumlahhari):
    return round (gajiperminggu / jumlahhari)

def gajiperjam(gajiperhari, jamkerja):
    return round (gajiperhari / jamkerja)

gajibulan = float(input("masukan gaji per bulan anda: "))
jamkerja = int(input("masukan jumlah jam kerja per hari: "))
jumlahhari = int(input("masukan jumlah hari kerja per minggu: "))

gaji_per_minggu = gajiperminggu(gajibulan)
gaji_per_hari = gajiperhari(gaji_per_minggu, jumlahhari)
gaji_per_jam = gajiperjam(gaji_per_hari, jamkerja)

print("== Nailah Rahmawati Yunus ==")
print("== 07352311121 ==")
print(f"gaji per minggu: {gaji_per_minggu}"''"rupiah")
print(f"gaji per hari: {gaji_per_hari}"''"rupiah")
print(f"gaji per jam: {gaji_per_jam}"''"rupiah")