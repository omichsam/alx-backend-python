from datetime import datetime
import sqlite3
import functools


def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get('query', args[0] if args else None)
            if query:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Executing SQL Query: {query}")
            else:
                print("No query provided.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
