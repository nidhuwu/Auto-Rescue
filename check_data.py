import sqlite3

def view_data():
    # Connect to SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Query all data from the users table
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Print the data
    if data:
        print("User Data:")
        for row in data:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Latitude: {row[4]}, Longitude: {row[5]}")
    else:
        print("No user data found.")

    # Close connection
    conn.close()

if __name__ == '__main__':
    view_data()
