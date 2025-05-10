#harga bensin

harga_pertalite = 10000
harga_pertamax = 12500
harga_solar = 6500
harga_pertamax_turbo = 15000

#tampilan

print("Selamat datang di SPBU")
print("")
print("|-------------------------|")
print("|   Pilihan Jenis BBM     |")
print("|-------------------------|")
print("|      Harga/1Liter       |")
print("|1.Pertalite   (Rp.10.000)|")
print("|2.Pertamax    (Rp.12.500)|")
print("|3.Solar       (Rp.6 .500)|")
print("|4.Max Turbo   (Rp.15.000)|")
print("|-------------------------|")
print("")

#identitas

nama = input("Nama: ")

pilihan = input("Pilihan 1/2/3/4: ")

jumlah_liter = float(input("Jumlah Liter: "))

if pilihan == "1":
    jenis_bbm = "Pertalite"
    harga_liter = harga_pertalite
elif pilihan == "2":
    jenis_bbm = "Pertamax"
    harga_liter = harga_pertamax
elif pilihan == "3":
    jenis_bbm = "Solar"
    harga_liter = harga_solar
elif pilihan == "4":
    jenis_bbm = "Pertamax Turbo"
    harga_liter = harga_pertamax_turbo
else :
    print("Mohon isi dengan benar")

total_harga = harga_liter * jumlah_liter

print(f"Harganya Rp.{total_harga} ya pak.")

ok = input(" ")
if ok == " ":
    print("syap")