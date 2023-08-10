"""
Crie um programa que diga se uma pessoa precisa se alistar ou não. Se não, 
há quanto tempo passou o prazo de alistamento e, se sim, quanto tempo falta 
para se alistar
"""

idade = int(input("Idade: "))

if idade < 18:
    print(f"Você deverá se alistar daqui há {18-idade} ano(s)")
elif idade > 18:
    print(f"Já passou {idade-18} ano(s) de seu alistamento")
else:
    print("Você deve se apresentar imediatamente ao programa de alistamento")

