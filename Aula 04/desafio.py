"""
Faça um programa que leia 3 retas de um usuário e diga se elas podem formar 
um triângulo
"""

# Entradas

com1 = int(input("Escreva o primeiro comprimento: "))
com2 = int(input("Escreva o segundo comprimento: "))
com3 = int(input("Escreva o terceiro comprimento: "))

# Resultados

if (com1 == com3) or (com1 == com2) or (com2 == com3):
    print("Sim, esses comprimentos podem formar um triângulo")
elif (com1**2==com2**2+com3**2) or (com2**2==com1**2+com3**2) or (com3**2==com2**2+com1**2):
    print("Sim, esses comprimentos podem formar um triângulo")
else:
    print("Não, esses comprimentos não podem formar um triângulo")

