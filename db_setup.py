import sqlite3

def drop_tables():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    
    # Drop the customer_suggestions table if it exists
    cursor.execute("DROP TABLE IF EXISTS customer_suggestions")
    cursor.execute("DROP TABLE IF EXISTS ingredient_inventory")
    cursor.execute("DROP TABLE IF EXISTS seasonal_flavors")
    
    conn.commit()
    conn.close()

def create_tables():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,s
        availability TEXT NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER NOT NULL,
        allergy_concern TEXT,
        FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors(id)
    )''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_tables()  # Drop existing tables
    create_tables()  # Create new tables
    print("Database and tables created successfully.")
