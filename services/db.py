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