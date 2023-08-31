"""
Defina uma classe BankAccount com atributos privados balance e account_number. 
Crie métodos deposit e withdraw para manipular o saldo
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def __str__(self):
        return f"Account Number: {self._account_number} \nBalance: {self._balance}"

    def deposit(self, value):
        if value < 0:
            print("Valor muito baixo")
            raise ValueError
        else:
            self._balance += value
            print(self)

    def withdraw(self, value):
        if value > self._balance:
            print("Valor muito baixo")
            raise ValueError
        else:
            self._balance -= value
            print(self)

