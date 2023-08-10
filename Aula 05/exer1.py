"""
Crie um programa que analise uma proposta de Financiamento Imobiliário. 
Se a prestação exceder 30% do salário, negue o financiamento
"""

casa = int(input("Digite o valor da casa: ")) 
salario = int(input("Digite o seu salário: "))
tempo = int(input("Digite em quantos anos você quer pagar: "))

prest = casa / (tempo * 12)

if prest > (salario * 0.3):
    print("Seu empréstimo foi negado")
else:
    print("Seu empréstimo foi aceito!")

