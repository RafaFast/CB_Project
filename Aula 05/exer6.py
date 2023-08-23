"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
"""

year = int(input("Birthday Year: "))

if 2023 - year <= 9:
    print("Categoria: Mirim")
elif 2023 - year <= 14:
    print("Categoria: Infantil")
elif 2023 - year <= 19:
    print("Categoria: Aprendiz")
elif 2023 - year <= 25:
    print("Categoria: Mestre")
else:
    print("Categoria: Grande Mestre")

