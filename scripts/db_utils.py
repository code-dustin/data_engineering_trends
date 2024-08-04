import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv()

def create_connection():
    try:
        connection = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")