class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount> balance:
        raise LowBalanceError("Insufficient Balance")

    return balance-amount



print(withdraw(105,101))
