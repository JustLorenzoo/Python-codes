# Atm
saldo_atm = 12e4
saldo_kartu = 1e7
notelp = "081312345678"
notelptuju = "081387654321"
pw = "123456"
user = "Asep" or "asep"
iya = "yes" or "Yes"

print("____________________________")
print("|____________o_____________|")
print("|  Selamat datang di Atm   |")
print("|--------------------------|")
print("|- Deposito             1.•|")
print("|- Menarik              2.•|")
print("|- Transfer             3.•|")
print("|- Lihat Tabungan       4.•|")
print("|- Lihat Kartu          5.•|")
print("|--------------------------|")
print("|__________________________|")
print("|        [1][2][3]         |")
print("|        [4][5][6]  _____  |")
print("|        [7][8][9] |_____| |")
print("|       [OK][0][NO]        |")
print("|__________________________|")
print("|       __________         |")
print("|        \/\/\/\/          |")
print("|       __________         |")
print("|__________________________|")
print(" ")

a = (input("Masukkan Kartu YES/NO: "))
if a == "yes" or "Yes":
    print("Mengidentifikasi")
    print(".")
    print(".")
    print("Kartu Diterima.")
else :
    print("INVALID")

u = (input("Username: "))
if u == "asep" or "Asep":
    print(".")
else :
    print("INVAILD")

b = (input("Masukkan Password: "))
if b == pw:
    print(".")
else :
    print("INVALID")

if a == "yes" or "Yes" and u == "asep" or "Asep" and b == "123456":
    print("Login Success")
else :
    print("INVALID!!")

c = (input("Pilihan 1 / 2 / 3 / 4 / 5: "))

if c == "1":
    print("Deposit (Selected)")
    jumlahdep = int(input("Jumlah Deposit: "))
    saldodep = jumlahdep + saldo_atm
    saldo_kartu_dep = saldo_kartu - jumlahdep
    print(f"Anda telah Dep sebesar Rp. {jumlahdep}")
    print(f"Saldo Kartu anda Rp. {saldo_kartu_dep}")

elif c == "2":
    print("Menarik (Selected)")
    jumlahtarik =int(input("Jumlah ingin DiTarik: "))
    saldotarik = saldo_atm - jumlahtarik
    saldo_kartu_tarik = saldo_kartu - jumlahtarik
    print(f"Anda telah menarik sebesar Rp. {jumlahtarik}")
    print(f"Saldo kartu anda Rp. {saldo_kartu_tarik}")

elif c == "3":
    print("Transfer (Selected)")
    print(".")
    print("Pilih Saldo awal")
    print("1. Saldo Kartu")
    print("2. Saldo Tabungan")
    pilihtf = input("1 / 2 : ")
    if pilihtf == "1":
        notuju = input("Nomor Tujuan: ")
        if notuju == "081387654321":
            jumlahtf = int(input("Jumlah Transfer: "))
            saldo_kartu_tf = saldo_kartu - jumlahtf
            print(f"Anda telah Mentransfer ke {notelptuju} sebesar Rp.{jumlahtf}.")
            saldo_tf = saldo_atm - jumlahtf
            print(f"Saldo Tabungan anda Adalah Rp.{saldo_tf}.")
    if pilihtf == "2":
        notuju = input("Nomor Tujuan: ")
        if notuju == "08138764321":
            jumlahtf = int(input("Jumlah Transfer: "))
            saldo_atm_tf = saldo_atm - jumlahtf
            print(f"Anda telah Mentransfer ke {notuju} sebesar Rp. {jumlahtf}")

elif c == "4":
    print("Lihat Tabungan (Selected)")
    print(f"Saldo Tabungan anda sebesar Rp.{saldo_atm}")

elif c == "5":
    print("Lihat Kartu (Selected)")
    print(f"Saldo kartu Anda sebesar Rp. {saldo_kartu}.")

else :
    print("INVALID")