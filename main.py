from Account import Account

account1 = Account(account_number=1, titular_name="Kevin", bank_balance=1500, credit_limit=500.99)
account2 = Account(account_number=2, titular_name="João", bank_balance=3000, credit_limit=785.33)
account3 = Account(account_number=3, titular_name="André", bank_balance=845.5, credit_limit=459.14)

#printing balance and name
account1.extract()
account2.extract()
account3.extract()

transfer_value = 250.11
print("{0} will transfer R$ {2:.2f} to {1}".format(account1.titular_name, account3.titular_name, transfer_value))
account1.transfer(250.11, account3)

#printing balance and name
account1.extract()
account2.extract()
account3.extract()