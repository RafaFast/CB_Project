"""
Desenvolva uma classe Rectangle com atributos width e height. Implemente um método 
calculate_area para calcular e retornar a área do retângulo.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"Area: {self.width * self.height}"

rect = Rectangle(7, 8)
print(rect.calculate_area())

