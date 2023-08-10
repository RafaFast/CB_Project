# Leia o primeiro termo e a razão de uma PA. Depois, mostre os 20 primeiros termos

ter1 = int(input("Primeiro termo: "))
raz = int(input("Razão: "))

for num_termo in range(1, 21):
    print(ter1 + (num_termo - 1) * raz, end = ", ")

