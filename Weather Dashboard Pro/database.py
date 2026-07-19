import sqlite3
def initialize_database():
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS favourites(
                id INTEGER PRIMARY KEY,
                city TEXT NOT NULL UNIQUE)
    ''')

    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS search_history(
                id INTEGER PRIMARY KEY,
                city TEXT NOT NULL,
                searched_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def add_favourite_city(city):
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO favourites(city) VALUES(?)",
            (city,)
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def view_favourite_cities():
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT city FROM favourites")
    favourite_cities = cursor.fetchall()
    conn.close()
    return favourite_cities

def delete_favourite_city(city):
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM favourites WHERE city = ?",
                   (city,))
        conn.commit()
        return cursor.rowcount > 0
    
    finally:
        conn.close()

def save_history(city):
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO search_history (city) VALUES (?)",(city,))
    conn.commit()
    conn.close()

def view_search_history():
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT city, searched_at FROM search_history ORDER BY searched_at DESC LIMIT 10")
    searched_cities = cursor.fetchall()
    conn.close()
    return searched_cities