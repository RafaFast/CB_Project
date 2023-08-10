"""
Faça um jogo de adivinhação onde o usuário escreve um  número e tenta 
acertar a escolha do computador
"""

import random

user = int(input("Escreva um número (0, 5): "))
pc = random.randint(0, 5)

if -1 < user < 6:
    if user == pc:
        print("Parabéns, você acertou!!")
    else:
        print("Não foi dessa vez... Tente novamente")
else:
    print("Apenas números entre 0 e 5")

