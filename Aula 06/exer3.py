"""
Desenvolva um programa que calcule a soma de todos números múltiplos de três 
entre 1 e 500
"""

mult = range(1, 500)
soma = 0

for mul in mult:
    if mul % 3 == 0:
        soma += mul

print(soma)

