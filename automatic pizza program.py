size = str(input("Enter the size of pizza:"))
bill = 0
rate = 8 
if size == "S":
    bill += 100
    print("small pizza prize will  be 100 :")
elif size == "M":
    bill += 200
    print("medium pizza prize will be 200 :")
elif size.lower() == 'l':
    bill += 300
    print("large pizza prize will be 300 :")
else :
    print("You have entered the wrong choice")

add_pepperoni = input("do you want pepperoni(Y/N):")

if add_pepperoni.lower() == 'y' or add_pepperoni.lower() == 'yes':
    print("Adding pepperoni to the pizza poppings")
    if size == 'S':
        bill += 30
    elif size == 'M':
        bill += 40
    else:
        bill += 50
    print("Added pepperoni to the pizza poppings")
elif add_pepperoni.lower() == 'n' or add_pepperoni.lower() == 'no':
    print("skipping the pepperoni .. as you have adopted no")
else:
    print("You have entered the wrong choice")

extra_cheese = input("do you want extra cheese(Y/N):")
if extra_cheese.lower() == 'y':
    if size == 'S':
        bill += 30
    elif size == 'M':
        bill += 40
    else:
        bill += 50
elif extra_cheese.lower() == 'n' or extra_cheese.lower() == 'no':
    print("skipping the extra cheese .. as you have adopted no")
else:
    print("You have entered the wrong choice")
print(f"your taxable value is {bill}")

tax = (bill * 8 )/100
print(f"your final bill is {int(bill+tax)}")