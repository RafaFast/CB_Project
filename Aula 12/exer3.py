"""
Escreva um programa que solicite ao usuário que digite seu nome e sua idade. Em seguida, 
tente converter a idade em um número inteiro. Se a conversão falhar informe ao usuário 
que a idade digitada é inválida e continue o programa. Caso contrário, exiba uma mensagem 
com o nome e a idade
"""

def main():
    print(f"\nName: {input('Write your name: ')} \nAge: {get_age()} \n")

def get_age():
    while True:
        try:
            return int(input("Write your age: "))
        except ValueError:
            print("Letters are not accepted")

main()

