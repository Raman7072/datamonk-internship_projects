import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 7. Average Rental Duration by Category (Bar Chart)
# ==============================

def Average_Rental():
    query = """
    SELECT c.name AS category, AVG(julianday(r.return_date) - julianday(r.rental_date)) AS avg_duration
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE r.return_date IS NOT NULL
        GROUP BY c.name
        ORDER BY avg_duration DESC;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(10,5))
    plt.bar(df['category'], df['avg_duration'], color='teal')
    plt.title("Average Rental Duration by Category")
    plt.xlabel("Category")
    plt.ylabel("Avg Duration (days)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv7.png")
    plt.close()

    conn.close()