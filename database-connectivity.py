import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the password from the environment variable
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Database connection details
db_config = {
    "host": "db-mysql-xxxxxxxxxxxxx15351184-0.m.db.ondigitalocean.com",
    "user": "doadmin",
    "password": "",  # Use the environment variable here
    "database": "defaultdb",
    "port": 25060,
    "ssl_disabled": False
}

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Continue with the rest of the code...

