"""
Crie uma função que receba uma lista de números como entrada e retorne o maior 
número presente na lista
"""

def major_num(lista):
    maior = lista[0]

    for n in lista:
        if n > maior:
            maior = n

    return maior

lista = [1, 3, 6, 87, 2, 4, 11, 256, 3]

print(major_num(lista))

