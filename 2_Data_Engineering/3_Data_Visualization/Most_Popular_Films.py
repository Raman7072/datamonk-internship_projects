import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)

# ==============================
# 2. Top 10 Most Popular Films (Bar Chart)
# ==============================
def Most_Popular_Films():

    query = """
    SELECT f.title, COUNT(r.rental_id) AS rental_count
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        GROUP BY f.title
        ORDER BY rental_count DESC
        LIMIT 10;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(10,5))
    plt.bar(df['title'], df['rental_count'], color='coral')
    plt.title("Top 10 Most Popular Films")
    plt.xlabel("Film")
    plt.ylabel("Rentals")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv2.png")
    plt.close()

    conn.close()