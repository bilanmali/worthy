from services.db import get_connection, save_subscription, get_all_subscriptions
from models.subscription import Subscription

def test_get_connection_returns_something():
    # check that calling get_connection actually gives us a connection object back
    connection = get_connection()
    assert connection is not None
    connection.close()
    

def test_save_subscription_adds_a_row():
    # create a subscription and save it, then check it actually landed in the database
    sub = Subscription("Netflix", 10.99, "2026-08-24", "Entertainment", "2026-08-01")
    save_subscription(sub)

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM subscriptions WHERE name = 'Netflix'")
    result = cursor.fetchone()
    connection.close()

    assert result is not None
    
def test_get_all_subscriptions_returns_a_list():
    # save one subscription, then check get_all_subscriptions finds it
    sub = Subscription("Spotify", 11.99, "2026-09-02", "Music", "2026-08-20")
    save_subscription(sub)

    subscriptions = get_all_subscriptions()

    assert len(subscriptions) > 0