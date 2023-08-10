"""
Crie um programa que calcule o aumento de salário de um funcionário. 
Se o salário for maior que R$1250,00 aumente em 15%, se não, aumente em 10%
"""

salario = int(input("Escreva o seu salário: "))

if salario > 1250:
    print(f"Seu salário, após o aumento, é R${salario*1.15}")
else:
    print(f"Seu salário, após o aumento, é R${salario*1.10}")

