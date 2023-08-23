# Leia o peso de 5 pessoas e mostre o maior e o menor peso digitado

lista = []

for n in range(5):
    peso = int(input("Peso: "))
    lista.append(peso)


print(f"\nMaior: {max(lista)} \nMenor: {min(lista)} \n") 

