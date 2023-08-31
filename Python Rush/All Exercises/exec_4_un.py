"""
Crie uma classe Student com atributos name, age e grades (uma lista). Adicione métodos 
para adicionar notas, calcular a média das notas e exibir as informações do aluno                                                                                                                                                                                                                                                                        
"""

class Student:
    def __init__(self, name, age, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

grades = list()
name = input("What's your name? ")
age = int(input("How old are you? "))

while True:
    while True:
        grades = input("What grade do you have? ")
        saida_grade = input("Have you finished [Y/N]? ").upper()
        if saida_grade == "Y":
            break

    for n in grades:
        i = dict()
        while True:
            i[n] = int(input(f"{i[n[:]]}'s Score: "))
            saida_score = input("Have you finished [Y/N]? ").upper()
            if saida_score == "Y":
                break
        
    break

print(grades)
    

    

