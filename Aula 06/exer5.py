"""
Crie um programa que receba 5 valores int e no final mostre a soma apenas 
dos pares
"""

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))
n4 = int(input("Escreva o quarto número: "))
n5 = int(input("Escreva o quinto número: "))

lista = [n1, n2, n3, n4, n5]
soma = 0

for n in lista:
    if n % 2 == 0:
        soma += n

print(f"Soma: {soma}")

