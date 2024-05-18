from enum import Enum


class Plan(Enum):
    BASIC = 19

    def __init__(self, subscription_cost):
        self.subscription_cost = subscription_cost
        self.tax_percentage = 20

    def charges(self):
        return self.subscription_cost + (self.subscription_cost * (self.tax_percentage / 100))
