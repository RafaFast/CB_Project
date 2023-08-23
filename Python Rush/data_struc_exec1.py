"""
Crie um programa que receba o nome e as notas(Duas) de 3 disciplinas de um aluno.
Armazene essas informações em um dicionário onde a chave é o nome da disciplina
e o valor é a sua nota. No final calcule a média das notas e exiba o nome do aluno, 
as disciplinas com suas respectivas notas e a média calculada.
"""

def main(): 
    aluno = {
        "name": input("Qual o seu nome? "),
        "math": [int(input("Score Math1: ")), int(input("Score Math2: "))],
        "sci": [int(input("Score Sci1: ")), int(input("Score Sci2: "))],
        "bio": [int(input("Score Bio1: ")), int(input("Score Bio2: "))]
    }

    aluno["score_math"] = (aluno["math"][0] + aluno["math"][1]) / 2
    aluno["score_sci"] = (aluno["sci"][0] + aluno["sci"][1]) / 2
    aluno["score_bio"] = (aluno["bio"][0] + aluno["bio"][1]) / 2

    print(*aluno)

main()

