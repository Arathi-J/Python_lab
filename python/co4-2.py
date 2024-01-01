class bank:
  def __init__(self, Acc_no, name,acc_type,Balance):
    self.Acc_no = Acc_no
    self.name = name
    self.acc_type = acc_type
    self.Balance = Balance
  def deposit(self,amt):
    if amt>0:
       self.Balance += amt
       print("Your successful Deposit = ",amt)
       print("New Balance = ",self.balance)
    else:
       print("Invalid")
  def withdrow_amt(self,damt):
    if 0<dmat<self.banance:
       self.Balance -= damt
       print("Successfully Withdrown amount = ",damt)
       print("New Balance = ",self.balance)
    elif damt>self.balance
       print("Insufficient funds. Withdrawal unsuccessful.")
    else:
       print("invalid input")
  def get_balance(self):
	return "Current balance: ${self.balance}"
       
acc1=Bank(123,"kunju","Savings",100)
print(account1.get_balance())
damt=int(input("Deposit amount"))
acc1.deposit(damt)
wamt=int(input("withdrow amount"))
acc1.deposit(wamt)

