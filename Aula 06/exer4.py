# Crie um programa que leia o número de um usuário e mostre sua tabuada (1x10)

num = int(input("Digite um número: "))

for n in range(1, 11):
    print(f"Número x {n} = {num * n}")

