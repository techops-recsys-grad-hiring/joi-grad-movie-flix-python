import unittest

from movieflix.models.customer import Customer
from movieflix.payments.payment import Payment
from movieflix.payments.upi_payment import UPIPayment


class TestPayment(unittest.TestCase):
    def test_should_calculate_charges_for_basic_plan_and_UPI_payment_for_non_premium_customer(self):
        expected_email = "test@test.com"
        payment_type = UPIPayment()
        payment = Payment()
        customer = Customer(expected_email, False)
        expected_total_charges = 24.8

        charges = payment.calculate_charges(customer, payment_type)

        self.assertEqual(expected_total_charges, charges)


if __name__ == '__main__':
    unittest.main()
