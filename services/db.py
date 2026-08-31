import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    # connect to PostgreSQL using the details stored in .env
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )
    return connection

def save_subscription(subscription):
    # save a subscription to the database
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO subscriptions (name, cost, renewalDate, category, lastUsedDate) VALUES (%s, %s, %s, %s, %s)",
        (subscription.name, subscription.cost, subscription.renewalDate, subscription.category, subscription.lastUsedDate)
    )
    connection.commit()
    connection.close()
    
def get_all_subscriptions():
    # fetch every subscription currently saved in the database
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, cost, renewalDate, category, lastUsedDate FROM subscriptions")
    rows = cursor.fetchall()
    connection.close()
    return rows