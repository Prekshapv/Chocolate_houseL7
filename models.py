import sqlite3

# Seasonal Flavors Functions
def add_seasonal_flavor(name, availability):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO seasonal_flavors (name, availability) VALUES (?, ?)", (name, availability))
        conn.commit()

def get_all_flavors():
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM seasonal_flavors")
        return cursor.fetchall()

def update_flavor_availability(name, availability):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE seasonal_flavors SET availability = ? WHERE name = ?", (availability, name))
        conn.commit()

def delete_flavor(name):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM seasonal_flavors WHERE name = ?", (name,))
        conn.commit()

# Ingredient Inventory Functions
def add_ingredient(name, quantity):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()

def update_ingredient(name, quantity):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE ingredient_inventory SET quantity = ? WHERE ingredient_name = ?", (quantity, name))
        conn.commit()

def get_all_ingredients():
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ingredient_inventory")
        return cursor.fetchall()

def delete_ingredient(name):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ingredient_inventory WHERE ingredient_name = ?", (name,))
        conn.commit()

# Customer Suggestions Functions
def add_customer_suggestion(flavor_suggestion, allergy_concern):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer_suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)", (flavor_suggestion, allergy_concern))
        conn.commit()

def get_all_suggestions():
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer_suggestions")
        return cursor.fetchall()

def delete_suggestion(suggestion_id):
    with sqlite3.connect('chocolate_house.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer_suggestions WHERE id = ?", (suggestion_id,))
        conn.commit()
