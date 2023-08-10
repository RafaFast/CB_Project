"""
Crie uma classe chamada 'Retângulo' que possua o método __init__ para inicializar as
propriedades 'largura' e 'altura' do retângulo. Em seguida, crie um objeto da classe 
'Retângulo' que calcule e imprima a área do retângulo
"""

class Retângulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

def main():
    retangulo = area_retang()
    area = (retangulo.altura * retangulo.largura)
    print(f"A área é: {area}")

def area_retang():
    largura = int(input("Largura: "))
    altura = int(input("Altura: "))
    return Retângulo(largura, altura)

main()

