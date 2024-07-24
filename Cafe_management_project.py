# Define the menu of the restaurant
menu= {'pizza':40,'pasta':50,'burger':60, 'salad':70,'coffee':80}
# greet
print("WELCOME JII to the python restaurant ! ")
print()
print( ' Pizza: Rs40 \n Pasta: Rs50 \n Burger: Rs60 \n Salad: Rs70 \n Coffee: Rs80')
print()
order_total =0
item_1=input(" Please enter your order  =  ")
print()

if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added !")
    print()
else:
    print(f"ordered item{item_1} not available:")
    print()
another_order=input("Do you want another item? (yes/no) :  ")
print()
if another_order=='yes':
    print()
    item_2 = input(" Please enter your second order = ")
    print()
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f" Your item {item_2} has been added to order !")
        print()
    else:
        print(f"ordered item {item_2} is not available ! Sorry")
        print()

print(f"Your total bill is :  {order_total}")
print()
print("Thank you for visiting us ! ")


