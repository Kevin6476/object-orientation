class Account:

    def __init__(self, account_number, titular_name, bank_balance, credit_limit):
        print(self)
        self.__account_number = account_number
        self.__titular_name = titular_name
        self.__bank_balance = bank_balance
        self.__credit_limit = credit_limit

    def extract(self):
        print("The account of '{0}' has a value of R$ {1:.2f}".format(self.__titular_name, self.__bank_balance))

    def __you_can_withdraw(self, amount_to_be_withdrawn):
        available_value = self.bank_balance + self.credit_limit
        return amount_to_be_withdrawn <= available_value

    def deposit(self, value):
        self.__bank_balance += value

    def to_withdraw(self, value):
        if self.__you_can_withdraw(value):
            self.__bank_balance -= value
        else:
            print("Operation not performed! Insufficient funds")

    def transfer(self, value, destination_account):
        if self.__you_can_withdraw(value):
            self.to_withdraw(value)
            destination_account.deposit(value)
            print("Transfer successful!")
        else:
            print("Operation not performed! Insufficient funds")

    @property
    def titular_name(self):
        return self.__titular_name

    @property
    def bank_balance(self):
        return self.__bank_balance

    @property
    def credit_limit(self):
        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        self.__credit_limit = credit_limit

    @staticmethod
    def bank_code():
        return "001"


