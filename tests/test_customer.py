import unittest
from movieflix.models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_should_create_non_premium_customer(self):
        expected_email = "test@test.com"

        customer = Customer(expected_email, False)

        self.assertEqual(customer.get_email(), expected_email)
        self.assertEqual(customer.get_is_premium_subscription(), False)

    def test_should_create_premium_customer(self):
        expected_email = "test@test.com"

        customer = Customer(expected_email, True)

        self.assertEqual(customer.get_email(), expected_email)
        self.assertEqual(customer.get_is_premium_subscription(), True)


if __name__ == '__main__':
    unittest.main()
