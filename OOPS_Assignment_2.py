class Account():

    def __init__(self, accountName, balanceAmount):
        self.AccountName = accountName
        self.BalanceAmount = balanceAmount

    def __str__(self):
        return 'Account Name : {}'.format(self.AccountName) + '\n' +'Account Balance: ${}'.format(self.BalanceAmount)

    
    def deposit(self, amount):
        self.BalanceAmount = self.BalanceAmount + amount
        print('Deposited your amount ${} to your account'.format(amount))

    def withdraw(self, amount):
        if(self.BalanceAmount - amount) <=0:
            print('Funds Unavailable')
        else:
            self.BalanceAmount = self.BalanceAmount - amount
            print('Withdrawal Accepted')

