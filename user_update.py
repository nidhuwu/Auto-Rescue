# import sqlite3

# def update_user_email(user_id, new_email):
#     # Connect to SQLite database
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()

#     # Update the email for a specific user
#     cursor.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, user_id))

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

# # Example usage: Update email for user with ID 1
# update_user_email(4, 'naragudehm@gmail.com')

#########33 location
import sqlite3

def update_user_location(user_id, new_lat, new_lon):
    # Connect to SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Execute the UPDATE statement
    cursor.execute('UPDATE users SET latitude = ?, longitude = ? WHERE id = ?', (new_lat, new_lon, user_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
user_id_to_update = 4  # replace with the actual user ID you want to update
new_latitude = 80.5  # replace with the new latitude
new_longitude = 85.2  # replace with the new longitude

update_user_location(user_id_to_update, new_latitude, new_longitude)