"""
Faça um programa que leia a latura e largura de uma parede e calcule sua área, 
mostre quantos litros de tinta será necessário para pintar sabendo que que 1L 
pinta 2x quadrados
"""

altura = float(input("Altura de sua parede: "))
largura = float(input("Largura de sua parede: "))

area = float((altura*largura))
tinta = float(area/2)

print(f"""Sua parede tem {area} metros e você vai precisar de {tinta} 
litros de tinta para pintá-la""")

