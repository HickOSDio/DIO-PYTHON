class BankAccount:
    def __init__(self):
        self.balance = 0
        self.limit = 500
        self.statement = ""
        self.withdrawals = 0
        self.WITHDRAWAL_LIMIT = 3

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.statement += f"Depósito: R$ {amount:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif amount > self.limit:
            print("Operação falhou! O valor do saque excede o limite.")
        elif self.withdrawals >= self.WITHDRAWAL_LIMIT:
            print("Operação falhou! Número máximo de saques excedido.")
        elif amount > 0:
            self.balance -= amount
            self.statement += f"Saque: R$ {amount:.2f}\n"
            self.withdrawals += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def print_statement(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.statement else self.statement)
        print(f"\nSaldo: R$ {self.balance:.2f}")
        print("==========================================")


def main():
    account = BankAccount()
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        option = input(menu)

        if option == "d":
            value = float(input("Informe o valor do depósito: "))
            account.deposit(value)

        elif option == "s":
            value = float(input("Informe o valor do saque: "))
            account.withdraw(value)

        elif option == "e":
            account.print_statement()

        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()