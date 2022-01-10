from User import User


class Customer(User):

    def __init__(self, name, customerID):
        super().__init__(name, customerID)

    itemList = {}
    total = 0

    def addItems(self, itemName, quantity, rate):
        if itemName not in self.itemList:
            self.itemList[itemName] = [quantity, rate, rate * quantity]
        else:
            self.itemList[itemName] = [quantity, rate, rate * quantity]

    def viewBill(self):
        print("Name \t", " Quantity \t", " Rate\t", " Price")
        for value in self.itemList:
            x = self.itemList[value]
            name = x[0]
            qty = x[1]
            amount = x[2]
            print(value, " \t\t", name, " \t\t", qty, " \t\t", amount, " \t\t")

        print("\n\nTotal Price: ", self.total)

    def check_calculateBill(self):

        for ele in self.itemList:
            x = self.itemList[ele]
            self.total += x[2]

        return self.total

    def check_itemExist(self, name):

        if name in self.itemList:
            return True
        else:
            return False

    def check_value_in_item(self, name, inCart):

        if name not in self.itemList:
            return False
        else:
            if self.itemList[name] == inCart:
                return True
            else:
                return False