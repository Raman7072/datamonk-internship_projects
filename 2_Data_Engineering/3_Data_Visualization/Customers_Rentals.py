import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 6. Top 5 Customers by Rentals (Bar Chart)
# ==============================

def Customers_Rentals():
    query = """
    SELECT c.first_name || ' ' || c.last_name AS customer, COUNT(r.rental_id) AS rental_count
        FROM rental r
        JOIN customer c ON r.customer_id = c.customer_id
        GROUP BY customer
        ORDER BY rental_count DESC
        LIMIT 5;
    """
    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(8,5))
    plt.bar(df['customer'], df['rental_count'], color='orange')
    plt.title("Top 5 Customers by Rentals")
    plt.xlabel("Customer")
    plt.ylabel("Number of Rentals")
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv6.png")
    plt.close()

    conn.close()