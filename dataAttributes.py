class BankAccount:
    apr = 1.2

print(BankAccount.__dict__)
print(BankAccount.apr)

acc_1 = BankAccount()
acc_2 = BankAccount()

print(acc_1 is acc_2)
print(acc_1.__dict__)
print(acc_2.__dict__)
print(acc_1.apr)
print(acc_2.apr)

BankAccount.account_type = 'Savings'
print(acc_1.account_type)
print(acc_2.account_type)

acc_1.apr = 0
print(acc_1.__dict__)
print(acc_2.__dict__)
print(acc_1.apr)
print(acc_2.apr)

setattr(acc_2, 'apr', 10)
print(acc_2.__dict__)
print(getattr(acc_2, 'apr'))

acc_3 = BankAccount()
print(getattr(acc_3, 'apr'))


acc_1.bank = 'Acme Savings & Loans'
print(acc_1.__dict__)
print(acc_2.__dict__)
print(BankAccount.__dict__)
print(type(BankAccount.__dict__))

acc_1 = BankAccount()
print(type(acc_1.__dict__))


class Program:
    language = 'Python'

p = Program()
print(p.__dict__)
p.__dict__['version'] = '3.7'
print(p.__dict__)
print(p.version)
print(getattr(p, 'version'))

p = Program()
#print(p.version)
p.version = '3.7'
print(p.version)
print(p.__dict__)

