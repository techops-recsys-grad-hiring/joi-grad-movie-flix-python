from movieflix.payments.payment_type import PaymentType


class UPIPayment(PaymentType):
    def processing_fee(self):
        return 2
