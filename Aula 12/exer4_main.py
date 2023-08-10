"""
Crie uma função chamada "read_file" que recebe o nome de um arquivo e tenta abri-lo 
para leitura. Se o arquivo não existir, capture a exceção FileNotFoundError e 
imprima uma mensagem amigável para o usuário
"""

def read_file(file):
    try:
        print(open(file, encoding='utf-8').read())
    except FileNotFoundError:
        print("O arquivo não foi encontrado... ;(")

read_file('Aula 12\\exer4_texto.txt')

