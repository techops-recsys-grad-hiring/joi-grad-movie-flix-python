import unittest

from movieflix.models.plan import Plan


class TestPlan(unittest.TestCase):
    def test_should_return_charges_for_basic_plan(self):
        expected_charges = 22.8

        actual_charges = Plan.BASIC.charges()

        self.assertEqual(expected_charges, actual_charges)


if __name__ == '__main__':
    unittest.main()
