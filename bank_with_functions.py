import textwrap

def display_menu():
    menu_options = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tStatement
    [na]\tNew Account
    [la]\tList Accounts
    [nu]\tNew User
    [q]\tQuit
    => """
    return input(textwrap.dedent(menu_options))

def make_deposit(current_balance, deposit_amount, transaction_history, /):
    if deposit_amount > 0:
        current_balance += deposit_amount
        transaction_history += f"Deposit:\tR$ {deposit_amount:.2f}\n"
        print("\n=== Deposit successful! ===")
    else:
        print("\n@@@ Operation failed! Invalid amount. @@@")

    return current_balance, transaction_history

def make_withdrawal(*, current_balance, withdrawal_amount, transaction_history, max_withdrawal, withdrawal_count, max_withdrawals):
    insufficient_balance = withdrawal_amount > current_balance
    exceeds_limit = withdrawal_amount > max_withdrawal
    exceeds_withdrawal_count = withdrawal_count >= max_withdrawals

    if insufficient_balance:
        print("\n@@@ Operation failed! Insufficient balance. @@@")

    elif exceeds_limit:
        print("\n@@@ Operation failed! Withdrawal exceeds limit. @@@")

    elif exceeds_withdrawal_count:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif withdrawal_amount > 0:
        current_balance -= withdrawal_amount
        transaction_history += f"Withdrawal:\t\tR$ {withdrawal_amount:.2f}\n"
        withdrawal_count += 1
        print("\n=== Withdrawal successful! ===")

    else:
        print("\n@@@ Operation failed! Invalid amount. @@@")

    return current_balance, transaction_history

def display_statement(current_balance, /, *, transaction_history):
    print("\n================ STATEMENT ================")
    print("No transactions made." if not transaction_history else transaction_history)
    print(f"\nBalance:\t\tR$ {current_balance:.2f}")
    print("==========================================")

def register_user(user_list):
    cpf = input("Enter CPF (numbers only): ")
    user = find_user(cpf, user_list)

    if user:
        print("\n@@@ User with this CPF already exists! @@@")
        return

    full_name = input("Enter full name: ")
    birth_date = input("Enter birth date (dd-mm-yyyy): ")
    address = input("Enter address (street, number - district - city/state abbreviation): ")

    user_list.append({"name": full_name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print("=== User successfully registered! ===")

def find_user(cpf, user_list):
    filtered_users = [user for user in user_list if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def open_account(branch, account_number, user_list):
    cpf = input("Enter user's CPF: ")
    user = find_user(cpf, user_list)

    if user:
        print("\n=== Account successfully opened! ===")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n@@@ User not found, account creation process terminated! @@@")

def display_accounts(account_list):
    for account in account_list:
        account_info = f"""\
            Branch:\t{account['branch']}
            A/C:\t\t{account['account_number']}
            Holder:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(account_info))


def run():
    MAX_WITHDRAWALS = 3
    BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    withdrawal_count = 0
    users = []
    accounts = []

    while True:
        option = display_menu()

        if option == "d":
            amount = float(input("Enter deposit amount: "))

            balance, statement = make_deposit(balance, amount, statement)

        elif option == "w":
            amount = float(input("Enter withdrawal amount: "))

            balance, statement = make_withdrawal(
                current_balance=balance,
                withdrawal_amount=amount,
                transaction_history=statement,
                max_withdrawal=limit,
                withdrawal_count=withdrawal_count,
                max_withdrawals=MAX_WITHDRAWALS,
            )

        elif option == "s":
            display_statement(balance, transaction_history=statement)

        elif option == "nu":
            register_user(users)

        elif option == "na":
            account_number = len(accounts) + 1
            account = open_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)

        elif option == "la":
            display_accounts(accounts)

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")


run()
