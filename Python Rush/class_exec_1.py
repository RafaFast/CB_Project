"""
Crie uma classe 'Estudante' que contenha os atributos 'name', 'age' e 'grade'. 
Instancie um objeto a esta classe e por fim crie um método para printar na tela 
esses atributos criados
"""

class Estudante:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nGrade: {self.grade}"

student = Estudante("Vitin", 19, 8)
print(student)

