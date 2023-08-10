# Crie um programa que calcule uma hipotenusa

from math import hypot

c1 = float(input("Digite o comprimento do primeiro cateto: ")) 
c2 = float(input("Digite o comprimento do segundo cateto: "))

print(f"O comprimento da hipotenusa é {hypot(c1, c2)}")

