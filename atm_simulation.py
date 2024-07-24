# to understand the concept of conditional statement
name=input("Please enter your name:")  # scanf,cin,scanner
print( 'Hello',name)
message = """ 
How may i help you sir.

Please select any one of them option:
Type 1 >>>>> CHECK BALANCE.
Type 2 >>>>> DEPOSIT.
Type 3 >>>>> WITHDRAWL.
""" 
print(message)
task= int(input('Please choose any option:'))    #typecasting of string into int
available_balance=5000
print(task)

if task >=1 and task <=3:       # type print b/w 1 to 3
    print('Welcome to you in virtual bank!')
    # nested if else
    if task==1:
       
        print("Thanks for visiting us , your available amount is :",available_balance)
        pass  # pass keyword used to overcome the  identation error when body of conditional statement  is not write 
    
    elif task==2:# ...these 3 dot are replacement of pass keyword
        deposit_amount=int((input("Please enter your deposit amount:")))
        if deposit_amount >=500:
            available_balance=available_balance+deposit_amount  #available balance+=deposit_amount
            print("You have successfully deposit your amount",deposit_amount)
            print("Thanks for visiting us ,your available balance is :",available_balance)
        else:
            print("Please deposit atleast 500 rupees!")

    else:
        withdrawl_amount=int((input("Please enter your withdrawl amount:")))
        if withdrawl_amount <=available_balance:
            available_balance=available_balance-withdrawl_amount  #available balance+=deposit_amount
            print("You have successfully withdraw your amount",withdrawl_amount)
            print("Thanks for visiting us ,your available balance is :",available_balance)
    

        else:
            print("Sorry you don not have sufficient amount for withdrawl!")
        
else:
    print("Please choose correct option!")    
