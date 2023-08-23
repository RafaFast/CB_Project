"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18,5  -   Abaixo do peso
18,5 até 25     -   Peso Ideal
25 até 30       -   Sobrepeso
30 até 40       -   Obesidade
Acima de 40     -   Obesidade Mórbida
"""

# Entradas 

altura = int(input("Altura em centímetros: "))
peso = int(input("Seu peso: "))

# Tratamento dos dados

altura /= 100

# Criando variáveis importantes

imc = peso / (altura * altura)

# Resultados

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

