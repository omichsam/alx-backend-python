#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "russ3509"
DB_NAME = "ALX_prodev"


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def stream_user_ages():
    """
    Generator that yields user ages one by one.
    """
    connection = get_db_connection()
    if connection is None:
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT age FROM user_data")
            for (age,) in cursor:
                yield age
    except Error as e:
        print(f"Error executing query: {e}")
    finally:
        if connection.is_connected():
            connection.close()


def calculate_average_age():
    """
    Calculate the average age using the stream_user_ages generator.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0

    return total_age / count


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
