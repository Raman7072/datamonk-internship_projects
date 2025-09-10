import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 8. Film Length vs Rental Count (Scatter Plot)
# ==============================
def Film_Rental():
    query = """
    SELECT f.length, COUNT(r.rental_id) AS rental_count
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        GROUP BY f.length;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(10,6))
    plt.scatter(df['length'], df['rental_count'], alpha=0.6, color='red')
    plt.title("Film Length vs Rental Count")
    plt.xlabel("Film Length (minutes)")
    plt.ylabel("Number of Rentals")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv8.png")
    plt.close()

    conn.close()