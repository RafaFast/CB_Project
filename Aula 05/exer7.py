"""
Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que 
tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
"""

# Entradas

com1 = int(input("Escreva o primeiro comprimento: "))
com2 = int(input("Escreva o segundo comprimento: "))
com3 = int(input("Escreva o terceiro comprimento: "))

# Tratamnto de entradas para o caso do triângulo escaleno da linha 27

pow_com1 = com1 * com1
pow_com2 = com2 * com2
pow_com3 = com3 * com3

# Resultados

if com1 == com2 == com3:
        print("Sim, esses comprimentos podem formar um triângulo e é um triângulo equilátero")
elif (com1 == com3) or (com1 == com2) or (com2 == com3):
    print("Sim, esses comprimentos podem formar um triângulo e é um triângulo isósceles")
elif (pow_com1 == pow_com3 + pow_com2) or (pow_com2 == pow_com3 + pow_com1) or (pow_com3 == pow_com2 + pow_com1):
    print("Sim, esses comprimentos podem formar um triângulo e é um triângulo escaleno")
else:
    print("Não, esses comprimentos não podem formar um triângulo")

