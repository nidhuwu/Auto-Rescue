# import sqlite3

# def delete_all_data():
#     # Connect to SQLite database
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()

#     # Delete all data from the users table
#     cursor.execute('DELETE FROM users')

#     # Commit changes and close connection
#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     delete_all_data()


##################33
import sqlite3

def delete_user(user_id):
    # Connect to the SQLite database
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()

    # Execute the SQL query to delete the user with the specified ID
    cursor.execute("DELETE FROM users WHERE id=?", (2,))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

# Replace 'your_database_name.db' with the actual name of your SQLite database
# Call the function with the user ID you want to delete
delete_user(1)
