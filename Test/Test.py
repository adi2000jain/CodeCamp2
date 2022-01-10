import unittest
from Customer import Customer
from User import User


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.userObject = User("Aditya", "96651")
        self.customerObject = Customer(self.userObject.name, self.userObject.customerId)

    def test_check_bill_calculation(self):
        self.customerObject.addItems("Egg", 2, 12)
        self.customerObject.addItems("Milk", 2, 24)
        x = self.customerObject.check_calculateBill()
        self.assertEqual(x, 2 * 12 + 2 * 24)

    def test_check_user_details(self):
        x = self.userObject.check_CustomerDetails()
        self.assertEqual(x, ["Aditya", "96651"])

    def test_check_in_lst_false(self):
        self.customerObject.addItems("Egg", 2, 12)
        self.assertFalse(self.customerObject.check_itemExist("Sugar"))

    def test_check_in_lst_true(self):
        self.customerObject.addItems("Egg", 2, 12)
        self.assertTrue(self.customerObject.check_itemExist("Egg"))

    def test_check_value_in_lst_wrt_key(self):
        self.customerObject.addItems("Egg", 2, 12)
        self.assertFalse(self.customerObject.check_value_in_item("Egg", [2, 26, 2 * 12]))


if __name__ == '__main__':
    unittest.main()
