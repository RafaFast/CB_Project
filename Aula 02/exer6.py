""" 
Faça um programa que leia a quantidade de dias e km rodados por um carro alugado, 
depois calcule o valor do contrato sabendo que cada dia custa 60 reais e cada km 
custa 15 centavos
""" 

dia = int(input("Por quantos dias o carro foi alugado?"))
kms = float(input("Quantos Km o carro rodou?"))

print(f"O contrato custa: R${(dia*60)+(kms*0.15)}")

