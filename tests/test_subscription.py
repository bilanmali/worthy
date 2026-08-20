from models.subscription import Subscription

def test_subscription_stores_name():
    # create a subscription and check the name was saved properly
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    assert sub.name == "Netflix"
    
def test_subscription_stores_cost():
    # create a subscription and check the cost was saved properly
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    assert sub.cost == 10.99

def test_subscription_stores_renewal_date():
    # create a subscription and check the renewal date was saved properly
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    assert sub.renewalDate == "2026-08-24"
    
def test_subscription_stores_category():
    # create a subscription and check the category was saved properly
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    assert sub.category == "Entertainment"    
    
def test_subscription_stores_last_used_date():
    # create a subscription and check the last used date was saved properly
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    assert sub.lastUsedDate == "2026-08-01"