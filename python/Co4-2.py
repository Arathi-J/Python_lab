class Bank:
  def __init__(self, Acc_no, name,acc_type,Balance):
    self.Acc_no = Acc_no
    self.name = name
    self.acc_type = acc_type
    self.Balance = Balance
  def deposit(self,amt):
    if amt>0:
       self.Balance += amt
       print("\nYour successful Deposit = ",amt)
       print("New Balance = ",self.Balance)
    else:
       print("Invalid")
  def withdrow_amt(self,damt):
    if 0<damt<=self.Balance:
       self.Balance -= damt
       print("\nSuccessfully Withdrown amount = ",damt)
       print("New Balance = ",self.Balance)
    elif damt>self.Balance:
       print("Not posible to withdrow\n")
    else:
       print("invalid input\n")
  def get_balance(self):
       print('Current balance:',self.Balance)
acc1=Bank(123,"kunju","Savings",100)
c=0
while c!=3:
	print("\nEnter your choice:\n 1. Deposit\n2.Withdrow\n3.Exit\n")
	c=int(input("choice = "))     
	
	print(acc1.get_balance())
	if c==1:
	  damt=int(input("Deposit amount="))
	  acc1.deposit(damt)
	elif c==2:
	  wamt=int(input("withdrowing amount="))
	  acc1.withdrow_amt(wamt)
	else:
	  print("Invalid Choice")
	


