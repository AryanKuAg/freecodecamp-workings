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
        mybudget = 0
        for i in self.ledger:
            mybudget += i["amount"]
        return mybudget

    def transfer(self, amount, other_budget):
        funds = 0
        for i in self.ledger:
            funds += i["amount"]
        if funds >= amount:
            self.ledger.append(
                {"amount": -amount, "description": "Transfer to " + str(other_budget.category)})
            other_budget.deposit(amount, "Transfer from" + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        print(self.category.center(30, "*"))
        total = 0
        for i in self.ledger:
            part1 = str(i["description"])[:24]
            part2 = str(i["amount"]) + \
                ".00" if "." not in str(i["amount"]) else str(i["amount"])
            total += i["amount"]
            print(part1 + str(part2)[:8])
        #####TOTAL#####
        zeroTotal = str(total) if "." in str(total) else str(total) + ".00"
        print("Total: ", zeroTotal)
