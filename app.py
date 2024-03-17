from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import time

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', registration_success=False)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    # Connect to SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist (just to be safe)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            latitude TEXT,
            longitude TEXT
        )
    ''')

    # Insert data into the table
    cursor.execute('INSERT INTO users (name, email, phone, latitude, longitude) VALUES (?, ?, ?, ?, ?)',
                   (name, email, phone, latitude, longitude))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Wait for 5 seconds before redirecting to the form
    time.sleep(1)

    return render_template('index.html', registration_success=True)

if __name__ == '__main__':
    app.run(debug=True)
