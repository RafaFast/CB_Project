"""
Escreva um programa que diga quanto de pedágio um carro deve pagar. Se for 
mais que 200km deve-se pagar 0.45 por km, se não 0.5
"""

distance = int(input("Quantos kilometros você andou? "))

if distance <= 200:
    print(f"Você deve pagar R${distance*0.5}")
else:
    print(f"Você deve pagar R${distance*0.45}")

