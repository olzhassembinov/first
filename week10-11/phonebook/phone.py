import psycopg2
import csv

# Database connection parameters
db_params = {
    'dbname': 'phonebase',
    'user': 'postgres',
    'password': '2004',
    'host': 'localhost',
    'port': '5433'
}

def connect_db():
    """Connect to the PostgreSQL database server."""
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error connecting to the database:", error)
        return None

def insert_data_from_csv(csv_file):
    """Insert data from a specified CSV file into the phonebook."""
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", row)
            conn.commit()
            print("Data inserted from CSV successfully.")
            display_phonebook()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error inserting data from CSV:", error)
            conn.rollback()
        finally:
            conn.close()

def manual_data_entry():
    """Manually enter data into the phonebook via console input."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                           (first_name, last_name, phone))
            conn.commit()
            print("Data inserted manually successfully.")
            display_phonebook()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error inserting data manually:", error)
            conn.rollback()
        finally:
            conn.close()

def update_data():
    """Update data in the phonebook."""
    user_id = input("Enter the ID of the user to update: ")
    new_phone = input("Enter new phone number: ")
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (new_phone, user_id))
            conn.commit()
            print("Data updated successfully.")
            display_phonebook()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error updating data:", error)
            conn.rollback()
        finally:
            conn.close()

def query_data():
    """Query data from the phonebook."""
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, first_name, last_name, phone FROM phonebook ORDER BY id")
            records = cursor.fetchall()
            display_records(records)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error querying data:", error)
        finally:
            conn.close()

def delete_data():
    """Delete data from the phonebook."""
    user_id = input("Enter the ID of the user to delete: ")
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM phonebook WHERE id = %s", (user_id,))
            conn.commit()
            print("Data deleted successfully.")
            display_phonebook()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error deleting data:", error)
            conn.rollback()
        finally:
            conn.close()

def display_phonebook():
    """Display all records in the phonebook."""
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, first_name, last_name, phone FROM phonebook ORDER BY id")
            records = cursor.fetchall()
            display_records(records)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error fetching data:", error)
        finally:
            conn.close()

def display_records(records):
    """Display records in a table format."""
    if records:
        headers = ["ID", "First Name", "Last Name", "Phone"]
        header_line = '| '.join(format(title, "<15") for title in headers)
        print(header_line)
        print('-' * len(header_line))
        for row in records:
            print('| '.join(format(str(field), "<15") for field in row))
    else:
        print("No data available in the phonebook.")

def main_menu():
    """Display the main menu and handle user inputs."""
    print("\nWelcome to the PhoneBook Program!")
    print("1: Insert data from CSV")
    print("2: Manually add a contact")
    print("3: Update a contact")
    print("4: Query all contacts")  
    print("5: Delete a contact")
    print("6: Display all contacts") 
    print("0: Exit the program")

def handle_user_input():
    """Handle user inputs based on the main menu choices."""
    while True:
        main_menu()
        choice = input("Please enter your choice (0-6): ")
        if choice == '1':
            csv_path = input("Enter the path to your CSV file: ")
            insert_data_from_csv(csv_path)
        elif choice == '2':
            manual_data_entry()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':  
            display_phonebook()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    handle_user_input()
