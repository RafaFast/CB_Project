# Crie um programa que jogue pedra, papel ou tesoura com alguém

from random import choice

user = input("Escolha Pedra [R], Papel [P] ou Tesoura [T]: ").upper()

pc = choice(["R", "P", "T"])

if user not in ["R", "P", "T"]:
    print("Você digitou uma letra não definida")
    exit()

print("\n")

if user == "T":
    print("Você: Tesoura")
elif user == "R":
    print("Você: Pedra")
else:
    print("Você: Papel")

if pc == "T":
    print("Computador: Tesoura")
elif pc == "R":
    print("Computador: Pedra")
else:
    print("Computador: Papel")

print("\n")

if user == pc:
    print("Deu Empate ;(")
elif user == "R" and pc == "P" or user == "T" and pc == "R" or user == "P" and pc == "T":
    print("Você perdeu...")
else:
    print("Você ganhou! Parabéns!")

print("\n")

