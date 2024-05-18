from abc import ABC, abstractmethod


class PaymentType(ABC):
    @abstractmethod
    def processing_fee(self):
        pass
