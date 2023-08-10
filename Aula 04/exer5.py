# Faça um programa que leia 3 valores e diga qual o maior e qual o menor

val1 = int(input("Escreva o primeiro número: "))
val2 = int(input("Escreva o segundo número: "))
val3 = int(input("Escreva o terceiro número: "))

if val1 >= val2 >= val3:
    print(f"\nO maior é: {val1} \nO menor é: {val3} \n")
elif val1 >= val3 >= val2:
    print(f"\nO maior é: {val1} \nO menor é: {val2} \n")
elif val2 >= val1 >= val3:
    print(f"\nO maior é: {val2} \nO menor é: {val3} \n")
elif val2 >= val3 >= val1:
    print(f"\nO maior é: {val2} \nO menor é: {val1} \n")
elif val3 >= val1 >= val2:
    print(f"\nO maior é: {val3} \nO menor é: {val2} \n")
else:
    print(f"\nO maior é: {val3} \nO menor é: {val1} \n")

