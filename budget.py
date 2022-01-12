# create a Category class
# having ledger list
class Category:
    ledger = []

    def __init__(self, category):
        self.category = category

    def deposit(self, amount, description=''):
        objectForLedger = {"amount": amount, "description": description}
        self.ledger.append(objectForLedger)

    def withdraw(self, amount, description=''):
        funds = 0
        for i in self.ledger:
            funds += i["amount"]
        if funds >= amount:
            objectForLedger = {"amount": -amount, "description": description}
            self.ledger.append(objectForLedger)
            return True
        else:
            return False

    def get_balance(self):
        pass

    def transfer(self, amount, budget):
        pass

    def check_funds(self, amount):
        pass
