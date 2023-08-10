"""
Melhore o jogo de adivinhação onde o computador "pensa" em um número. Mostre quantos 
palpites o usuário usou
"""

from random import randint

def main():
    pc =  randint(1, 10)
    tentativas = []
    while True:
        user = int(input("Escreva um número: "))
        if user == pc:
            print(f"Você acertou! \n Você tentou {len(tentativas)} vezes")
            break
        else:
            tentativas.append(user)
            print("Tente novamente")

main()

