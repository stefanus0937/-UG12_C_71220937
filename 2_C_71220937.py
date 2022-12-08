def hitung(nilai,angka):
    str = ""
    for angka in nilai:
        str = nilai.count(angka)
    return str

nilai = str(input("Masukan angka : "))
angka = str(input("Masukan angka yg dihitung : "))

print("Angka",angka,"muncul sebanyak",hitung(nilai,angka),"kali")


