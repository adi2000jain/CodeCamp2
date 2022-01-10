class User:

    def __init__(self, name, customerID):
        self.name = name
        self.customerId = customerID

    def check_CustomerDetails(self):
        return [self.name, self.customerId]