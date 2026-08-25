import mysql.connector
import os
from dotenv import load_dotenv

# load the values from .env into the environment
load_dotenv()

def get_connection():
    # connect to MySQL using the details stored in .env
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
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