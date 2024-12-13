import mysql.connector
import uuid
import csv


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "russ3509"


def connect_db():
    """Connects to the MySQL database server."""
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        connection.commit()
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL."""
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database="ALX_prodev",
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None


def create_table(connection):
    """Creates the user_data table if it does not exist."""

    try:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS user_data ("
            "user_id VARCHAR(36) PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL,"
            "age INT NOT NULL"
            ")"

        )

        connection.commit()
        print("Table user_data created or already exists.")

    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def insert_data(connection, csv_filepath):
    """Inserts data into the user_data table from a CSV file."""
    try:
        with open(csv_filepath, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            data_to_insert = []
            for row in csv_reader:
                user_id = str(uuid.uuid4())
                name = row[0]
                email = row[1]
                age = int(row[2])
                data_to_insert.append((user_id, name, email, age))
        cursor = connection.cursor()
        sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, data_to_insert)
        connection.commit()
        print(f"{cursor.rowcount} rows inserted.")

    except FileNotFoundError:
        print(f"Error: {csv_filepath} not found.")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")


def data_generator(connection, chunk_size=1000):
    """
    Generates rows from the user_data table in chunks.
    """
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data"
        cursor.execute(query)

        while True:
            rows = cursor.fetchmany(chunk_size)
            if not rows:
                break
            yield from rows

    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")
