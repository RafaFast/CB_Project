"""
Crie uma classe chamada Person com atributos name e age, e um método display_info 
que imprime o nome e a idade da pessoa.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")
    
person = Person("Vitin", 19)
person.display_info

