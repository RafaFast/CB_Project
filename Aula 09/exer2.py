"""
Crie um dicionário que guarde o nome, ano de nascimento, idade, ano de contratação 
e o salário de um funcionário. Calcule e acrescente no dicionário em quantos anos a 
pessoa se aposentará
"""

def main():
    data = {
        'nome': input("Qual o seu nome? "),
        'ano_nasc': int(input("Em qual ano você nasceu? ")),
        'ano_contr': int(input("Qual foi o ano de contratação? ")),
        'salario': float(input("Qual o seu salário? "))
    }
    
    data['idade'] = 2023 - data['ano_nasc']
    data['aposentadoria'] = 65 - data['idade']
    
    print(data)

main()

