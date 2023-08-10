"""
Escreva um programa que peça ao usuário para digitar um número inteiro e, em seguida, 
imprima o dobro desse número. Utilize try/except para lidar com a possibilidade de o 
usuário inserir um valor não numerico
"""

while True:
    try:
        number = int(input("Number: "))
        print(2 * number)
        break
    except ValueError:
        print("Just Numbers")

