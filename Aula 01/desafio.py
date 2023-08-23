# Faça um programa que leia um número e diga se ele é ímpar ou par sem utilizar condicionais

num = int(input("Num: "))

treat1 = (num * 3) + 1
treat2 = treat1 % 2

print(num, "Its A", treat2 == 0, "Odd Number,", "It Is A", treat2 != 0, "Even Number")

