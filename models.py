import sqlite3

def get_db_connection():
    conn = sqlite3.connect('chocolate_house.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_seasonal_flavor(name, availability):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO seasonal_flavors (name, availability) VALUES (?, ?)", (name, availability))
        conn.commit()
        return cursor.lastrowid

def get_all_flavors():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM seasonal_flavors")
        return [dict(flavor) for flavor in cursor.fetchall()]

def update_flavor_availability(name, availability):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE seasonal_flavors SET availability = ? WHERE name = ?", (availability, name))
        conn.commit()

def delete_flavor(name):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM seasonal_flavors WHERE name = ?", (name,))
        conn.commit()

def add_ingredient(name, quantity):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()

def update_ingredient(name, quantity):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE ingredient_inventory SET quantity = ? WHERE ingredient_name = ?", (quantity, name))
        conn.commit()

def get_all_ingredients():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ingredient_inventory")
        return [dict(ingredient) for ingredient in cursor.fetchall()]

def delete_ingredient_by_id(ingredient_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ingredient_inventory WHERE id = ?", (ingredient_id,))
        conn.commit()

def add_customer_suggestion(flavor_id, allergy_concern):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer_suggestions (flavor_id, allergy_concern) VALUES (?, ?)", (flavor_id, allergy_concern))
        conn.commit()

def get_all_suggestions():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer_suggestions")
        return [dict(suggestion) for suggestion in cursor.fetchall()]

def delete_suggestion(suggestion_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer_suggestions WHERE id = ?", (suggestion_id,))
        conn.commit()

def delete_flavor_by_id(flavor_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM seasonal_flavors WHERE id = ?", (flavor_id,))
        conn.commit()