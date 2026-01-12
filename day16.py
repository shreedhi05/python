#nesting
#calculator
# num1=int(input("enter first number"))
# num2=int(input("enter "))


#atmm - withdrawal , - depositi , - balance cheque
balance=1000
atm=int(input("enter 1 for withdrawal 2 for deposit 3 for balance cheque"))

if atm==1:
    amount=int(input("enter a amount"))
    if amount>0 and amount<=balance:
        print(amount-balance)
    else:
        print("moneyless")

elif atm==2:
    amount=int(input("enter a paisa"))
    if amount<0 :
        print(balance+amount)
    else:
        print("invalid amount")

elif atm==3:
    print(balance)

else:
    print("broke")

