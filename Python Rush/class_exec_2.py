"""
Crie uma classe 'BankAccount' que inicialize com 'account_number' e 'balance'.
Depois crie um método para sacar e outro para depositar. Após isso, teste criando 
dois objetos em que um saca e, o outro, deposita certos valores. Mostre as mudanças
na tela
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(self)

    def __str__(self):
        return f"\nAccount Number: {self.account_number} \nBalance: {self.balance}"
    
    # Métodos

    def withdraw(self, value):
        self.balance -= value
        print(self)

    def deposit(self, value):
        self.balance += value
        print(self)

# Definindo os objetos
student_1 = BankAccount(12345, 1340)
student_2 = BankAccount(54321, 4560)

# Chamando os métodos

while True:
    saque = int(input("\nSacar: "))
    if saque <= student_1.balance:
        student_1.withdraw(saque)
    else:
        print("\nSaque maior do que o valor na conta!")
        raise ValueError
    
    depositar = int(input("\nDepositar: "))
    if depositar >= 0:
        student_2.deposit(depositar)
    else:
        print("\nSaque maior do que o valor na conta!")
        raise ValueError
    
    sair = input("Quer sair? [Y/N]").upper()
    if sair == "Y":
        break

