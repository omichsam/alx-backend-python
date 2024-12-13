#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "russ3509"
DB_NAME = "ALX_prodev"


@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            buffered=True
        )
        yield connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()


def stream_users():
    """
    Generator function to stream rows from the user_data table one by one.
    """
    with get_db_connection() as connection:
        if connection is None:
            return

        try:
            with connection.cursor(dictionary=True, buffered=True) as cursor:
                cursor.execute("SELECT * FROM user_data")
                for row in cursor:
                    yield row
        except Error as e:
            print(f"Error executing query: {e}")


if __name__ == "__main__":
    for user in stream_users():
        print(user)
