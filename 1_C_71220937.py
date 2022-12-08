#soal 1
def terbalik(x):
    sum = ""
    for i in x:
        sum = i + sum
    return sum

x = input("Masukan Kata atau angka : ")
print(terbalik(x))