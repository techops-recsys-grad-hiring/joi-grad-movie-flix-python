import unittest
from movieflix.models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_should_create_non_premium_customer(self):
        customer = Customer("Test", False)

        self.assertEqual(customer.get_email(), "Test")
        self.assertEqual(customer.get_is_premium_subscription(), False)

    def test_should_create_premium_customer(self):
        customer = Customer("Test", True)

        self.assertEqual(customer.get_email(), "Test")
        self.assertEqual(customer.get_is_premium_subscription(), True)


if __name__ == '__main__':
    unittest.main()
