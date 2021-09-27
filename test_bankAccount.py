from bankAccount import BankAccount

def test_should_return_account_information():
    name = "Ranga Gonnage"
    account_number = "1207199419111996"
    account_balance = 10
    bankAccount = BankAccount(name, account_number, account_balance)
    
    expected_result = {"name": name, 
                       "account_number": account_number,
                       "account_balance": account_balance}
    assert bankAccount.account_informations() == expected_result

def test_should_withdraw():
    name = "Ranga Gonnage"
    account_number = "1207199419111996"
    account_balance = 1000
    bankAccount = BankAccount(name, account_number, account_balance)
    bankAccount.withdraw(100)

    expected_result = 900
    assert bankAccount.account_balance == expected_result

def test_should_deposit():
    name = "Ranga Gonnage"
    account_number = "1207199419111996"
    account_balance = 1000
    bankAccount = BankAccount(name, account_number, account_balance)
    bankAccount.deposit(100)

    expected_result = 1100
    assert bankAccount.account_balance == expected_result