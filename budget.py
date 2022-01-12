import math
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


###############
def create_spend_chart(category_list):  # (list) -> string
    # upto four category
    cat_withdraw = []
    total_withdraw = 0

    for i in category_list:
        funds = 0
        for j in i.ledger:
            if j["amount"] < 0:
                funds += j["amount"]
        total_withdraw += -funds
        cat_withdraw.append(-funds)

    withdraw_percentage = []  # useful list here 1 - 10
    for i in cat_withdraw:
        data = math.floor(i/total_withdraw) * 10
        withdraw_percentage.append(data)

    ###########################
    print("Percentage spent by category")
    mylist = withdraw_percentage
    nname = category_list.category
    for i in range(100, -1, -10):
        addzero = ''
        for zero in mylist:
            if i/10 <= zero:
                addzero += "o  "
            else:
                addzero += "   "
        print(" " * (3 - len(str(i))) + str(i)+"| " + addzero)
    print("    -" + '---' * len(mylist))

    mymax = 0
    for i in nname:
        mymax = max(mymax, len(i))

    for i in range(mymax):
        cat_name = ''
        for name in nname:
            if len(name) - 1 >= i:
                cat_name += name[i] + "  "
            else:
                cat_name += "   "
        print(" " * 5+cat_name)
