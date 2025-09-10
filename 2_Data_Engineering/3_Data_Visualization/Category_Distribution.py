import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 3. Category Distribution (Pie Chart)
# ==============================
def Category_Distribution():
    
    query = """
    SELECT c.name AS category, COUNT(r.rental_id) AS rental_count
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        GROUP BY c.name
        ORDER BY rental_count DESC;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(8,8))
    plt.pie(df['rental_count'], labels=df['category'], autopct='%1.1f%%', startangle=140)
    plt.title("Rental Distribution by Category")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv3.png")
    plt.close()

    conn.close()