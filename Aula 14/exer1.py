"""
Crie uma classe chamada 'Cachorro' que possua o método __init__ para inicializar as
propriedades 'nome' e 'idade' do cachorro. Em seguida, crie um objeto da classe 'Cachorro' 
e imprima o nome e a idade do cachorro
"""

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def main():
    catchoro = entrada()
    print(f"Nome: {catchoro.nome}, Idade: {catchoro.idade}")

def entrada():
    nome = input("Nome: ")
    idade = input("Idade: ")
    return Cachorro(nome, idade)

main()

"""
Ou:

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def main():
    catchoro = entrada("Vitin", 19)
    print(f"Nome: {catchoro.nome}, Idade: {catchoro.idade}")

def entrada(nome, idade):
    return Cachorro(nome, idade)

main()
"""

