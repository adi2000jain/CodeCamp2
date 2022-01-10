from Customer import Customer
from User import User

name = input("Enter Customer Name: ")
id = input("Enter ID: ")
obj = User(name, id)

n = 0
ob1 = Customer(obj, name)
while True:
    quantity = 0
    rate = 0
    choice = 0

    choiceCheckType = False
    while not choiceCheckType:
        try:
            choice = int(input("\n Enter 1 To Add Item \n Enter 2 Calculate Bill\n"))

            if choice == 1 or choice == 2:
                choiceCheckType = True
            else:
                print("Please Enter Choice Either 1 or 2")
        except ValueError:
            print("Please Enter Choice Either 1 or 2")

    if choice == 1:
        itemName = input("Enter Item Name: ")

        checkQuantityType = False
        while not checkQuantityType:
            try:
                quantity = int(input("Enter Quantity: "))

                if isinstance(quantity, int) and quantity > 0:
                    checkQuantityType = True
                elif quantity <= 0:
                    print("Quantity should be greater than 1")
            except ValueError:
                print("Please enter valid Number")

        checkRateType = False
        while not checkRateType:
            try:
                rate = float(input("Enter Rate: "))

                if isinstance(rate, float) and rate > 0:
                    checkRateType = True
                elif rate <= 0:
                    print("Quantity should be greater than 0")
            except ValueError:
                print("Please enter valid Rate")

        ob1.addItems(itemName, quantity, rate)
        n += 1
        continue

    elif choice == 2:
        ob1.check_calculateBill()
        print(ob1.viewBill())
        print("Total Number of Item: ", n)
        print("Customer Name: ", name, " Customer Id: ", id)
        break

    else:
        break