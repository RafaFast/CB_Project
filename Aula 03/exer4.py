# Escreva um programa que escolha qual, dentre quatro alunos, apagará o quadro

import random

alu1 = input("Escreva o nome do primeiro aluno: ")
alu2 = input("Escreva o nome do segundo aluno: ")
alu3 = input("Escreva o nome do terceiro aluno: ")
alu4 = input("Escreva o nome do quarto aluno: ")

print(f"O aluno que apagará o quadro é: {random.choice([alu1, alu2, alu3, alu4])}")

