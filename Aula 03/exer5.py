# Crie um programa que crie uma ordem aleatória de fila com quatro alunos

from random import shuffle

alu1 = input("Escreva o nome do primeiro aluno: ")
alu2 = input("Escreva o nome do segundo aluno: ")
alu3 = input("Escreva o nome do terceiro aluno: ")
alu4 = input("Escreva o nome do quarto aluno: ")

alunos = [alu1, alu2, alu3, alu4]

shuffle(alunos)

print(alunos)

