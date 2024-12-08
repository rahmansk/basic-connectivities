import mysql.connector

# Database connection details
db_config = {
    "host": "db-mysql-xxxxxxxxxxxxxxx351184-0.m.db.ondigitalocean.com",
    "user": "doadmin",
    "password": "",  # Replace with your actual password
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

# Create the `tasks` table if it doesn't exist
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task_name VARCHAR(100) NOT NULL,
        description TEXT,
        status ENUM('Pending', 'Completed') DEFAULT 'Pending'
    );
    """
    cursor.execute(query)
    connection.commit()
    print("Table `tasks` created successfully (if not already present).")

# Add a new task
def add_task(task_name, description):
    query = "INSERT INTO tasks (task_name, description) VALUES (%s, %s)"
    cursor.execute(query, (task_name, description))
    connection.commit()
    print("Task added successfully!")

# View all tasks
def view_tasks():
    query = "SELECT id, task_name, description, status FROM tasks"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n--- To-Do List ---")
        for row in results:
            print(f"ID: {row[0]}, Task: {row[1]}, Description: {row[2]}, Status: {row[3]}")
    else:
        print("\nNo tasks found.")

# Mark a task as completed
def complete_task(task_id):
    query = "UPDATE tasks SET status = 'Completed' WHERE id = %s"
    cursor.execute(query, (task_id,))
    connection.commit()
    print(f"Task ID {task_id} marked as completed!")

# Delete a task
def delete_task(task_id):
    query = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(query, (task_id,))
    connection.commit()
    print(f"Task ID {task_id} deleted successfully!")

# Main menu
def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            description = input("Enter task description: ")
            add_task(task_name, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    create_table()  # Ensure the table exists
    main()

# Close the connection when done
cursor.close()
connection.close()

