from movieflix.models.plan import Plan


class Customer:
    def __init__(self, email, is_premium_subscription):
        self.email = email
        self.is_premium_subscription = is_premium_subscription
        self.selected_plan = Plan.BASIC

    def get_email(self):
        return self.email

    def get_is_premium_subscription(self):
        return self.is_premium_subscription

    def get_selected_plan(self):
        return self.selected_plan
