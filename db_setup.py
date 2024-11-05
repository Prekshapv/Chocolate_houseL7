import sqlite3

def initialize_db():
    try:
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()

        # Seasonal Flavors table
        cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            availability TEXT
                            )''')

        # Ingredient Inventory table
        cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                            id INTEGER PRIMARY KEY,
                            ingredient_name TEXT NOT NULL,
                            quantity INTEGER NOT NULL
                            )''')

        # Customer Suggestions table
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                            id INTEGER PRIMARY KEY,
                            flavor_suggestion TEXT,
                            allergy_concern TEXT
                            )''')

        conn.commit()
        print("Database initialized and tables created.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    initialize_db()
