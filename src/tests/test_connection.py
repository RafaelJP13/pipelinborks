from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

def test_connection():

    connection = None
    try:
        connection = mysql.connector.connect(

            host = os.getenv("MYSQL_HOST"),
            user = os.getenv("MYSQL_USER"),
            password = os.getenv("MYSQL_PASSWORD"),
            database = os.getenv("MYSQL_DATABASE")

        )

        if connection.is_connected():
            print("Connected to MySQL server")
    except Error as e:
        print(e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
