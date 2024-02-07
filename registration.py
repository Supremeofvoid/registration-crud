import sqlite3
from datetime import datetime

DATABASE_NAME = 'registration.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Registration (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT NOT NULL,
                            Email TEXT NOT NULL,
                            DateOfBirth DATE
                      )''')
    conn.commit()
    conn.close()

def create_registration(name, email, dob):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Registration (Name, Email, DateOfBirth)
                          VALUES (?, ?, ?)''', (name, email, dob))
        conn.commit()
        print("Registration added successfully!")
    except sqlite3.Error as e:
        print("Error adding registration:", e)
    finally:
        conn.close()

def get_all_registrations():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Registration''')
        registrations = cursor.fetchall()
        return registrations
    except sqlite3.Error as e:
        print("Error retrieving registrations:", e)
    finally:
        conn.close()

def update_registration(reg_id, name, email, dob):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''UPDATE Registration SET Name=?, Email=?, DateOfBirth=?
                          WHERE ID=?''', (name, email, dob, reg_id))
        conn.commit()
        print("Registration updated successfully!")
    except sqlite3.Error as e:
        print("Error updating registration:", e)
    finally:
        conn.close()

def delete_registration(reg_id):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Registration WHERE ID=?''', (reg_id,))
        conn.commit()
        print("Registration deleted successfully!")
    except sqlite3.Error as e:
        print("Error deleting registration:", e)
    finally:
        conn.close()

def main():
    create_table()

    while True:
        print("\n1. Add Registration")
        print("2. View All Registrations")
        print("3. Update Registration")
        print("4. Delete Registration")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            try:
                dob = datetime.strptime(dob, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                continue
            create_registration(name, email, dob)
        elif choice == '2':
            registrations = get_all_registrations()
            if registrations:
                print("\nAll Registrations:")
                for reg in registrations:
                    print(reg)
            else:
                print("No registrations found!")
        elif choice == '3':
            reg_id = input("Enter Registration ID to update: ")
            name = input("Enter Updated Name: ")
            email = input("Enter Updated Email: ")
            dob = input("Enter Updated Date of Birth (YYYY-MM-DD): ")
            try:
                dob = datetime.strptime(dob, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                continue
            update_registration(reg_id, name, email, dob)
        elif choice == '4':
            reg_id = input("Enter Registration ID to delete: ")
            delete_registration(reg_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
