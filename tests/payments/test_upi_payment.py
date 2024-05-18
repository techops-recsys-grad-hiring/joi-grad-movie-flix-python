import unittest

from movieflix.payments.upi_payment import UPIPayment


class TestUPIPayment(unittest.TestCase):
    def test_should_return_processing_fee_for_UPI_payment(self):
        payment_type = UPIPayment()

        processing_fee = payment_type.processing_fee()

        self.assertEqual(2, processing_fee)


if __name__ == '__main__':
    unittest.main()
