"""
Crie uma classe Student com atributos name, age e grades (uma lista). Adicione métodos 
para adicionar notas, calcular a média das notas e exibir as informações do aluno                                                                                                                                                                                                                                                                        
"""

class Student:
    def __init__(self, name, age, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

grades = dict()
name = input("What's your name? ")
age = int(input("How old are you? "))

while True:
    grades = input("What grade do you have? ")
    grade_score = int(input(""))
    saida = input("Do you want to leave [Y/N]? ").upper()
    if saida == "Y":
        break
