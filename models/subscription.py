class Subscription:
    def __init__(self, name, cost, renewalDate, category, lastUsedDate):
        # store the subscription's name
        self.name = name
        # store the subscription's monthly cost
        self.cost = cost
        # store the subscription's renewal date
        self.renewalDate = renewalDate
        # store the subscription's category
        self.category = category
        # store the subscription's last used date
        self.lastUsedDate = lastUsedDate