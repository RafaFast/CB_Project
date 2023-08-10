"""
Crie uma função chamada 'divide_numbers' que recebe dois parâmetros númericos '(a, b)' 
e retorna a divisão de 'a' por 'b'. Utilize try/except para tratar a divisão por 0
"""

def divide_numbers():
    while True:
        try:
            x = int(input("Numerator: "))
            y = int(input("Denominator: "))
            return float(x / y)
        except ZeroDivisionError:
            print("There's no number divisible by zero")
        except ValueError:
            print("Only numbers are accepted")

print(divide_numbers())

