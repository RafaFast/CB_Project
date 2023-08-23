# Mostre o fatorial de uma entrada do usuário

def main():
    num = int(input("Number: "))

    for n in range(num - 1, 1, -1):
        num *= n

    print(num)

main()

