import mysql.connector
import pytest
config={
        'database': 'expense_tracker',
        'user': 'root',
        'password': 'root',
        'host': 'localhost',  # Set the host where your MySQL server is running
        'port': '3306',  #
}

@pytest.fixture
def getConnection():
    conn=None
    try:
        conn=mysql.connector.connect(**config) # ** is used to tell python to unpack the dictionary and send it as keyword arguments
        print("connection established")
        yield conn
    except mysql.connector.errors as e:
        print(f"error occurred- {e}")
    finally:
        if conn:
            conn.close()




