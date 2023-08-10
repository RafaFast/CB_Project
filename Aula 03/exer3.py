# Faça um programa que diga o seno, cosseno e tangente de um ângulo

import math

angulo = int(input("Escreva o ângulo: "))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"""
    O cosseno de {angulo} é: {cosseno} 
    O seno de {angulo} é: {seno} 
    A tangente de {angulo} é: {tangente}
""")

