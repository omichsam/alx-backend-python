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


def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows in batches from the user_data table.
    """
    with get_db_connection() as connection:
        if connection is None:
            return

        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM user_data")
                while True:
                    batch = cursor.fetchmany(batch_size)
                    if not batch:
                        break
                    yield batch
        except Error as e:
            print(f"Error executing query: {e}")


def batch_processing(batch_size):
    """
    Process each batch to filter users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)


if __name__ == "__main__":
    batch_processing(50)
