class BankAccount:
    accounts = []
    def __init__(self,int_rate,account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        if(self.account_balance - amount) >= 0:
            self.account_balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance: {self.account_balance}')
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()

savings = BankAccount(0.05,1200)
checking = BankAccount(0.03,800)

savings.deposit(200).deposit(100).deposit(300).withdraw(500).yield_interest().display_account_info()
checking.deposit(60).deposit(30).withdraw(80).withdraw(240).withdraw(160).withdraw(40).yield_interest().display_account_info()

BankAccount.print_all_accounts()