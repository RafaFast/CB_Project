from random import randint

for n in range(30):
    carros = list()
    distance = dict()
    for i in range(30):
        avanco_a = randint(1, 6)
        avanco_b = randint(1, 6)
        distance['carro_a'] += avanco_a.copy()
        distance['carro_b'] += avanco_b.copy()
        carros.append(distance)
        print(f"Carro A avançou {avanco_a} posições")
        print(f"Carro B avançou {avanco_b} posições")
        print(*distance.items())

        if distance['carro_a'] >= 30:
            print("Car A its the winner!!")
            break
        elif distance['carro_b'] >= 30:
            print("Car B its the winner!!")
            break


