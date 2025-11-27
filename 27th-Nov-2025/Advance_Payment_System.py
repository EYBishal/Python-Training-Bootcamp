
class Payment:
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def create_id(self):
        print(f"Your payment ID is {self.name}@123")

    def pay(self, pay_amount):
        if self.amount >= pay_amount:
            self.amount -= pay_amount
            print(f"{pay_amount} has been paid")
            print(f"Your total balance left is {self.amount}")
        else:
            print("You don't have enough money")
            s = input("Do you want to check your balance? (yes/no): ")
            if s.lower() == "yes":
                print("Balance is:", self.amount)
            else:
                print("Thank you")


class GooglePay(Payment):
    def __init__(self, amount, name):
        super().__init__(amount, name)
        self.history = []

    def googlepay(self):
        while True:
            g = int(input("Press 1 to initiate payment, 2 to check history, 3 to create ID, 4 to exit: "))

            if g == 1:
                amt_input = input("Enter amount to pay: ")
                if amt_input.isdigit():
                    amt = int(amt_input)
                    self.pay(amt)
                    self.history.append(f"Paid {amt}")
                else:
                    print("Invalid amount! Please enter a number.")
            elif g == 2:
                print("Payment History:", self.history)
            elif g == 3:
                self.create_id()
            elif g == 4:
                print("Exiting Google Pay...")
                break
            else:
                print("Invalid choice")


class AmazonPay(Payment):
    def __init__(self, amount, name):
        super().__init__(amount, name)
        self.history = []

    def amazonpay(self):
        while True:
            g = int(input("Press 1 to initiate payment, 2 to check history, 3 to create ID, 4 to exit: "))

            if g == 1:
                amt_input = input("Enter amount to pay: ")
                if amt_input.isdigit():
                    amt = int(amt_input)
                    self.pay(amt)
                    self.history.append(f"Paid {amt}")
                else:
                    print("Invalid amount! Please enter a number.")
            elif g == 2:
                print("Payment History:", self.history)
            elif g == 3:
                self.create_id()
            elif g == 4:
                print("Exiting Amazon Pay...")
                break
            else:
                print("Invalid choice")


class PayTMPay(Payment):
    def __init__(self, amount, name):
        super().__init__(amount, name)
        self.history = []

    def paytmpay(self):
        while True:
            g = int(input("Press 1 to initiate payment, 2 to check history, 3 to create ID, 4 to exit: "))

            if g == 1:
                amt_input = input("Enter amount to pay: ")
                if amt_input.isdigit():
                    amt = int(amt_input)
                    self.pay(amt)
                    self.history.append(f"Paid {amt}")
                else:
                    print("Invalid amount! Please enter a number.")
            elif g == 2:
                print("Payment History:", self.history)
            elif g == 3:
                self.create_id()
            elif g == 4:
                print("Exiting PayTM Pay...")
                break
            else:
                print("Invalid choice")


# Main Menu
i = input("Enter your choice of UPI Payment:\n1 for Google Pay\n2 for Amazon Pay\n3 for PayTM Pay\n")
if i.isdigit():
    i = int(i)
    if i == 1:
        g = GooglePay(1000, "Bishal")
        g.googlepay()
    elif i == 2:
        a = AmazonPay(1000, "Bishal")
        a.amazonpay()
    elif i == 3:
        p = PayTMPay(1000, "Bishal")
        p.paytmpay()
    else:
        print("Invalid choice")
else:
    print("Invalid input! Please enter a number.")
