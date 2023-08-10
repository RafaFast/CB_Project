"""
Faça um programa que calcule a média de um aluno e diga se ele aprovou 
(nota maior ou igual a 7), está em recuperação (entre 5 e 7), ou reprovou 
(menor que 5)
"""

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média foi {media} e você está devidamente Aprovado!")
elif 5 <= media < 7:
    print(f"Sua média foi {media}, você está em recuperação")
    print(f"Sua média foi {media}, você está reprovado")

