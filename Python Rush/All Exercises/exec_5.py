"""
Defina uma classe Car com atributos make, model e year. Crie um método start_engine que 
imprime uma mensagem indicando que o motor foi iniciado.
"""

from time import sleep

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    
    @classmethod
    def get(cls):
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        return cls(make, model, year)


    def start_engine(self):
        print(self, "\n...", end="")
        sleep(4)
        print("\nYour car is already started")

def main():
    car = Car.get()
    car.start_engine()
    
main()
