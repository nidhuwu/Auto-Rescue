import sqlite3
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

def get_nearest_user(accident_lat, accident_lon):
    # Connect to SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Query all data from the users table
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()

    # Close connection
    conn.close()

    nearest_user = None
    min_distance = float('inf')

    for user in users_data:
     user_id = user[0]
     user_name = user[1]
    
    # Convert latitude and longitude to float
    user_lat = float(user[4])  # assuming latitude is in the 5th column
    user_lon = float(user[5])  # assuming longitude is in the 6th column

    distance = haversine(accident_lat, accident_lon, user_lat, user_lon)

    if distance < min_distance:
        min_distance = distance
        nearest_user = {'id': user_id, 'name': user_name, 'distance': distance}


    return nearest_user

if __name__ == '__main__':
    # Fixed coordinates for the accident (replace with actual accident coordinates)
    accident_latitude = 72.101
    accident_longitude = 71.508

    nearest_user = get_nearest_user(accident_latitude, accident_longitude)

    if nearest_user:
        print(f"The nearest user is User ID {nearest_user['id']} ({nearest_user['name']}) with a distance of {nearest_user['distance']} km.")
        # You can now access the details of the nearest user using nearest_user['id'], nearest_user['name'], etc.
    else:
        print("No registered users found.")
