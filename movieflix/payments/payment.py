from movieflix.models.customer import Customer
from movieflix.payments.payment_type import PaymentType


class Payment:
    def calculate_charges(self, customer: Customer, payment_type: PaymentType):
        return customer.get_selected_plan().charges() + payment_type.processing_fee()
