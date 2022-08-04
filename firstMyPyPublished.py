inp_nama = input("input your name : ")

print(f"hey {inp_nama}, nice to meet you.")
print("\n")
cc = input("i have a simple calculator, want to try? [y/n]")


print(cc)

if cc == "y":
    #latihan membuat kalkulator sederhana

    #kalkulator sederhana
    print("\n======Simple Calculator======")



    angka_1 = float(input("input first number = "))
    operator = input("operator (+,-,x,/) :")
    angka_2 = float(input("input srcpnd number = "))

    #percabangannya

    if operator == "+":
        hasil = angka_1 + angka_2
        print(f"= {hasil}")
    elif operator == "-":
        hasil = angka_1 - angka_2
        print(f"= {hasil}")
    elif operator == "x" or operator == "*":
        hasil = angka_1 * angka_2
        print(f"= {hasil}")
    elif operator == "/":
        hasil = angka_1 / angka_2
        print(f"= {hasil}")
    else:
        print("please input a correct number! ")


    print("\n")
    print("[hasil dari program, terima kasih]")


if cc == "n":
    print("alright mate,nice to meet you, bye")

