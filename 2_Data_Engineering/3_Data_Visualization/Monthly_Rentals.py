import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

SCREENSHOT_DIR = "screenshots"
DB_PATH = "sakila.db"

conn = sqlite3.connect(DB_PATH)


# ==============================
# 1. Monthly Rentals Over Time (Line Chart)
# ==============================
def Monthly_Rentals():
         
    query = """
    SELECT strftime('%Y-%m', rental_date) AS month, COUNT(*) AS rentals
        FROM rental
        GROUP BY month
        ORDER BY month;
    """

    df = pd.read_sql_query(query, conn)

    plt.figure(figsize=(10,5))
    plt.plot(df['month'], df['rentals'], marker='o', color='skyblue')
    plt.title('Monthly Rentals Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Rentals')
    plt.xticks(rotation = 45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{SCREENSHOT_DIR}/dv1.png")
    plt.close()

    conn.close()