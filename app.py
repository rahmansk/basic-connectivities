import mysql.connector

# Database connection details
db_config = {
    "host": "xxxxxxxxxxxxxx15351184-0.m.db.ondigitalocean.com",
    "user": "doadmin",
    "password": "",  # Replace with your actual password
    "database": "defaultdb",
    "port": 25060,  # DigitalOcean MySQL port
    "ssl_disabled": False  # Ensures SSL is enabled as required by DigitalOcean
}

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Function to insert data into the database
def insert_user(name, email):
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    connection.commit()
    print("User data inserted successfully!")

# Function to retrieve all users from the database
def fetch_users():
    query = "SELECT id, name, email FROM users"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n--- User Data ---")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    else:
        print("No users found.")

# Main menu
def main():
    while True:
        print("\n1. Add User")
        print("2. View Users")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            insert_user(name, email)
        elif choice == "2":
            fetch_users()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    );
    """
    cursor.execute(query)
    connection.commit()
    print("Table `users` created successfully (if not already present).")

create_table()

# Run the main menu
if __name__ == "__main__":
    main()

# Close the connection when done
cursor.close()
connection.close()

