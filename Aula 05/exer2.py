# Crie um conversor para Binário, Octal ou Hexadecimal

num = int(input("Digite um número: "))
base = input("Binário / Octal / Hexadecimal [B, O, H]: ").upper()

if base == "B":
    print(f"O número {num} é, em Binário: {bin(num)[2:]}")
elif base == "O":
    print(f"O número {num} é, em Octal: {oct(num)[2:]}")
else:
    print(f"O número {num} é, em Hexadecimal: {hex(num)[2:]}")

