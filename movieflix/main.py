from movieflix.models.customer import Customer
from movieflix.payments.payment import Payment
from movieflix.payments.upi_payment import UPIPayment


class MovieFlix:
    def interact_with_user(self):
        print("\n#-----------Movieflix subscription plan-----------#")
        print("Supported plan : BASIC\nSupported Payment: UPI\n")
        consent = input("Enter yes to subscribe\n")
        if consent.lower() == "yes":
            customer = self.get_customer_details()
            payment_type = UPIPayment()
            payment = Payment()
            total_charges = payment.calculate_charges(customer, payment_type)
            print("Total charges: {}".format(total_charges))
        else:
            print("Thank you please enter yes to subscribe")

    def get_customer_details(self):
        email = input("Enter registered email id\n")
        is_premium_customer = input("Enter yes if premium customer\n")
        is_premium_subscription = is_premium_customer == "yes" if True else False
        return Customer(email, is_premium_subscription)


if __name__ == '__main__':
    movieFlix = MovieFlix()
    movieFlix.interact_with_user()
