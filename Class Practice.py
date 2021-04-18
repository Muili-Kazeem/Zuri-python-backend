class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount_to_deposit):
        self.amount = self.amount + amount_to_deposit
        return "you deposited " + str(amount_to_deposit)

    def withdraw(self, amount_to_withdraw):
        self.amount = self.amount - amount_to_withdraw
        return "you withdrew " + str(amount_to_withdraw)

    def transfer(self):
        pass

    def check_balance(self):
        return "Your budget balance is " + str(self.amount)